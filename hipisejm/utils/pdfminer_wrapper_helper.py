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
