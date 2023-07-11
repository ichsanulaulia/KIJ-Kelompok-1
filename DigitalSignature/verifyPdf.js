const keyPair = require('./signature');
const fs = require('fs')
const pdfParse = require('pdf-parse')
const crypto = require('crypto')


const  key = keyPair.getPublickKey()
const filePDF = `./pdf.pdf`

   try {
    const data = fs.readFileSync("signature.json", "utf8");
    // console.log(JSON.parse(data).signature);
   const assigm = JSON.parse(data).signature
       const verif = crypto.createVerify('SHA256');
       verif.update(filePDF)
       verif.end();

    const result = verifier.verify(key, assigm, 'hex');
    console.log('Digital Signature Verification : ' + result);    

} catch (err) {
    console.error(err);
}





