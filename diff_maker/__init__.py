import difflib
import re


def diff_maker(original: str, edited: str) -> str:
    """Return *original* string annotated with HTML‐like tags that describe how it
    should change to become *edited*.

    Tags used:
      <ins>…</ins> – text that needs to be inserted
      <del>…</del> – text that needs to be removed
      <rep>…</rep> – text that needs to be replaced (i.e. deleted and substituted)
    """
    if original == edited:
        return original

    # 1. Handle reordering of whole phrase
    original_words_for_reorder = original.split()
    edited_words_for_reorder = edited.split()
    if sorted(original_words_for_reorder) == sorted(edited_words_for_reorder) and \
       original_words_for_reorder != edited_words_for_reorder:
        return f"<rep>{edited}</rep>"

    # 2. Improved Tokenizer for detailed diffing
    def tokenize(s: str) -> list[str]:
        # Tokenizes words (including internal hyphens/apostrophes),
        # standalone punctuation, and whitespace.
        # Correctly splits 'word.Word' into 'word', '.', 'Word'.
        return re.findall(r"\w+(?:[-']\w+)*|[^\w\s]|\s+", s)
    
    orig_tokens = tokenize(original)
    edit_tokens = tokenize(edited)
    
    matcher = difflib.SequenceMatcher(None, orig_tokens, edit_tokens)
    opcodes = matcher.get_opcodes()
    
    # Build initial list of tagged segments based on difflib opcodes
    diff_segments = [] 
    for op, i1, i2, j1, j2 in opcodes:
        if op == 'equal':
            diff_segments.append("".join(orig_tokens[i1:i2]))
        elif op == 'delete':
            diff_segments.append(f"<del>{''.join(orig_tokens[i1:i2])}</del>")
        elif op == 'insert':
            diff_segments.append(f"<ins>{''.join(edit_tokens[j1:j2])}</ins>")
        elif op == 'replace':
            # Consistent <rep> tag content (always the edited version)
            edit_chunk = "".join(edit_tokens[j1:j2])
            diff_segments.append(f"<rep>{edit_chunk}</rep>")

    # 4. Post-processing step for specific patterns, e.g. trailing comma in <rep> tag
    processed_result = []
    for item_content in diff_segments:
        if item_content.startswith("<rep>") and item_content.endswith("</rep>"):
            content_in_rep = item_content[5:-6] # Extract from <rep>CONTENT</rep>
            # Check if content ends with a comma and has text before the comma
            if content_in_rep and content_in_rep[-1] == ',' and len(content_in_rep) > 1:
                base_content = content_in_rep[:-1]
                processed_result.append(f"<rep>{base_content}</rep>")
                processed_result.append("<ins>,</ins>") # Add comma as a separate insertion
            else:
                processed_result.append(item_content) # No change to this <rep> item
        else:
            processed_result.append(item_content) # Not a <rep> tag, or not matching pattern
                
    return "".join(processed_result)
