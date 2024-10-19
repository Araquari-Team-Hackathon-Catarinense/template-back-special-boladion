import magic

CONTENT_TYPE_PDF = ["application/pdf"]
CONTENT_TYPE_IMAGES = ["image/png", "image/jpeg", "image/jpg", "image/webp"]
CONTENT_TYPE_DOCUMENTS = CONTENT_TYPE_PDF + CONTENT_TYPE_IMAGES


def get_content_type(file):
    if hasattr(file, "temporary_file_path"):
        content_type = magic.from_file(file.temporary_file_path(), mime=True)
    else:
        content_type = magic.from_buffer(file.read(), mime=True)

    if hasattr(file, "seek") and callable(file.seek):
        file.seek(0)

    return content_type
