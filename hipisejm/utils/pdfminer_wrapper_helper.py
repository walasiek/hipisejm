from hipisejm.utils.pdfminer_wrapper import PDFText, PDFLineBreak, PDFTextBoxBreak, PDFPageBreak


def get_first_text_box_from_index(raw_parsed_list, index=0, with_breaking_box=False):
    return get_first_pdf_container_from_index(PDFTextBoxBreak, raw_parsed_list, index=index, with_breaking_box=with_breaking_box)


def get_first_page_from_index(raw_parsed_list, index=0, with_breaking_box=False):
    return get_first_pdf_container_from_index(PDFPageBreak, raw_parsed_list, index=index, with_breaking_box=with_breaking_box)


def get_first_pdf_container_from_index(pdf_container_type, raw_parsed_list, index=0, with_breaking_box=False):
    """
    Extracts all entries between <ContainerBreak>
    which surrounds given index.
    If index points out to ContainerBreak
    then returns all elements in the container before it.
    Params:
       pdf_container_type - PDFTextBoxBreak, PDFLineBreak or PDFPageBreak
       raw_parsed_list - list of elements to get text box
       index - index to check for surrounding elements
       with_breaking_box - if set to True then last extracted index is breaking (closing) Element (useful to get metadata from it)
    """
    assert pdf_container_type in [PDFTextBoxBreak, PDFLineBreak, PDFPageBreak]

    result = []
    after_elements = []
    before_elements = []

    if not isinstance(raw_parsed_list[index], pdf_container_type):
        for entry in raw_parsed_list[index+1:]:
            if isinstance(entry, pdf_container_type):
                if with_breaking_box:
                    after_elements.append(entry)
                break
            else:
                after_elements.append(entry)
        result.append(raw_parsed_list[index])
    else:
        if with_breaking_box:
            result.append(raw_parsed_list[index])

    if index > 0:
        for entry in reversed(raw_parsed_list[:index]):
            if isinstance(entry, pdf_container_type):
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
