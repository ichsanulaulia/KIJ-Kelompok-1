import verifyPDF from '@ninja-labs/verify-pdf';
const signedPdfBuffer = fs.readFileSync('pdf.pdf');

const {
    verified,
    authenticity,
    integrity,
    expired,
    meta
} = verifyPDF(signedPdfBuffer);