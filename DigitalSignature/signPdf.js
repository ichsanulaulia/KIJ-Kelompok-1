const keyPair = require('./keyPair');
const fs = require('fs')
const pdfParse = require('pdf-parse')
const crypto = require('crypto')

const filePDF = `./dummy.pdf`
const fileSign='./signature.json'



main()



function setSignature(signature){
    
    const signatureJSON = {
        'signature': signature
    }
    fs.writeFileSync(fileSign,JSON.stringify(signatureJSON,null,4))
}



async function createSign(filePath,privateKey){
    const sign = crypto.createSign('SHA256')
    sign.update(filePDF)
    sign.end()
    const signature = sign.sign(privateKey).toString('hex')
    setSignature(signature)
    console.log('Generated Signature: ',signature)
}

async function main(){
    key = await keyPair.getPrivateKey()
    if (!process.argv[2]){
        createSign(filePDF,key)
    }
    else{
        createSign(process.argv[2],key)
    }
}

