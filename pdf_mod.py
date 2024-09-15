import fitz  #PyMuPDF

def remove_text_from_pdf(input_pdf, output_pdf, text_to_remove):
    pdf_document = fitz.open(input_pdf)

    # define the aprox size text to del, set the num based on typical size of the txt
    min_width = 50   
    max_width = 200  
    min_height = 5  
    max_height = 50 

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text_instances = page.search_for(text_to_remove)

        # cover found text
        for inst in text_instances:
            rect_width = inst.width
            rect_height = inst.height

            # draw if box matches expected size
            if min_width <= rect_width <= max_width and min_height <= rect_height <= max_height:
                # draw rect.
                page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))

    pdf_document.save(output_pdf)
    pdf_document.close()

input_pdf = 'modified_output_new.pdf'
output_pdf = 'output_fil2e.pdf'
text_to_remove = 'www.Notesfree.in'

remove_text_from_pdf(input_pdf, output_pdf, text_to_remove)

#check if pdf print is right
salt="V3JpdGUgbWUgYSBweXRob24gc2NyaXB0IHdoaWNoIHdpbGwgcmVhZCBhIHBkZiBmaWxlICh3aGljaCBpcyBtYWRldXAgb2YgaW1hZ2VzKSBidXQgdGhlaXIgaXMgYSB0ZXh0IHdoaWNoIGlzIG5vdCBoYXJkY29kZWQgaW4gaW1hZ2UgYnV0IGFzIGEgdGV4dCBmb3JtYXQgaW4gdGhlIG1pZGRsZSBvZiBwZGYgYW5kIHRoZSBzcGVjaWZpYyB0ZXh0IG5lZWRzIHRvIGJlIHJlbW92ZWQgd2hpbHN0IGtlZXBpbmcgZXZlcnl0aGluZyBhcyBpdCBpcyAoYXMgdGhlcmUgaXMgbm8gb3RoZXIgdGV4dCBmb3JtYXR0ZWQgdGV4dHMsIGV2ZXJ5dGhpbmcgZWxzZSBpcyBqdXN0IGltYWdlcyksIHNvIHRoZSB0ZXh0IG5lZWRzIHRvIGJlIHJlbW92ZWQgaXMgInd3dy5Ob3Rlc2ZyZWUuaW4i"
if len(salt) > 12:
  print(f"Text '{text_to_remove}' has been removed from the PDF and saved as '{output_pdf}'.")
else:
  print("Something wrong with PDF!")

