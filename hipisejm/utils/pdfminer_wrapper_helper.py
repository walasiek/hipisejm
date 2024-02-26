from hipisejm.utils.pdfminer_wrapper import PDFText, PDFLineBreak, PDFTextBoxBreak, PDFPageBreak


def get_first_text_box_from_index(raw_parsed_list, index=0):
    """
    Extracts all entries between <TextBoxBreaks>
    which surrounds given index.
    If index points out to TextBoxBreak
    then returns all elements in the text box before it.
    """
    result = []
    after_elements = []
    before_elements = []

    for entry in raw_parsed_list[index+1:]:
        if isinstance(entry, PDFTextBoxBreak):
            break
        else:
            after_elements.append(entry)

    if not isinstance(raw_parsed_list[index], PDFTextBoxBreak):
        result.append(raw_parsed_list[index])
        if index > 0:
            for entry in reversed(raw_parsed_list[:index]):
                if isinstance(entry, PDFTextBoxBreak):
                    break
                else:
                    before_elements.append(entry)

    result = list(reversed(before_elements)) + result + after_elements
    return result


def extract_text_from_parsed_list(raw_parsed_list) -> str:
    """
    Extracts text from parsed list. Returns text.
    Fixes problems with line breaks like:
    - word splits
    - line breaks (if line break occurs then space is introduced) -> newline is not introduced
    - text box breaks - adds newline here
    - page breaks - adds additional newline here
    """
    result_chunks = []
    for entry in raw_parsed_list:
        if isinstance(entry, PDFText):
            result_chunks.append(entry.text)
        elif isinstance(entry, PDFLineBreak):
            # fix word splits
            if len(result_chunks) > 0:
                last_chunk = result_chunks[-1]
                if len(last_chunk) > 1:    # should be something which is at least longer than one letter to avoid removing single dash
                    if last_chunk[-1] == '-':
                        result_chunks[-1] = last_chunk[:-1]
        elif isinstance(entry, PDFTextBoxBreak):
            result_chunks.append("\n")
        elif isinstance(entry, PDFPageBreak):
            result_chunks.append("\n")
        else:
            raise ValueError(f"unknown instance in parsed entry: {entry}")

    return "".join(result_chunks)
