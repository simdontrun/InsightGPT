from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(
    report_text,
    output_file
):

    doc = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            story.append(
                Spacer(
                    1,
                    6
                )
            )

    doc.build(
        story
    )

    print(
        f"PDF generated: {output_file}"
    )