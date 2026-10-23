const fs = require('fs');
const {createCanvas, loadImage} = require('@napi-rs/canvas');
(async () => {
 const html = fs.readFileSync(__dirname+'/dist/index.html', 'utf8');
 const icons = [...html.matchAll(/<svg[^>]*>[\s\S]*?<\/svg>/g)].map(m=>m[0]);
 const canvas=createCanvas(600,100),ctx=canvas.getContext('2d');
 ctx.fillStyle='#faf7ef';ctx.fillRect(0,0,600,100);
 for(let i=0;i<icons.length;i++) {
  const svg=icons[i].replaceAll('currentColor','#876728');
  const img=await loadImage(Buffer.from(svg));
  ctx.drawImage(img,i*100+25,25,50,50);
 }
 fs.writeFileSync(__dirname+'/icon-library-preview.png',canvas.toBuffer('image/png'));
})();
