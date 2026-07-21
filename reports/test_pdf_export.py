from reports.executive_report_generator import (
    generate_executive_report
)

from reports.pdf_exporter import (
    export_pdf
)


report = generate_executive_report()

export_pdf(
    report,
    "reports/Executive_Report.pdf"
)