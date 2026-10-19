(() => {
const svg=document.querySelector('svg');
function bb(el){const b=el.getBBox();const m=el.getCTM();const p=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>{const q=svg.createSVGPoint();q.x=x;q.y=y;return q.matrixTransform(m)});return {x0:Math.min(...p.map(a=>a.x)),y0:Math.min(...p.map(a=>a.y)),x1:Math.max(...p.map(a=>a.x)),y1:Math.max(...p.map(a=>a.y))}}
const clipR={x0:30,y0:110,x1:650,y1:1010};
const units=[];
for(const g of svg.querySelectorAll('[filter]')){const b=bb(g);const w=b.x1-b.x0,h=b.y1-b.y0;units.push({t:g.textContent.slice(0,40),b:{x0:b.x0-0.04*w,x1:b.x1+0.04*w,y0:b.y0-0.08*h,y1:b.y1+0.08*h},el:g,plated:true})}
for(const t of svg.querySelectorAll('text')){if(t.closest('[filter]'))continue;units.push({t:t.textContent.slice(0,40),b:bb(t),el:t,plated:false})}
const ov=(a,b)=>a.x0<b.x1-0.5&&b.x0<a.x1-0.5&&a.y0<b.y1-0.5&&b.y0<a.y1-0.5;
const res=[];
for(let i=0;i<units.length;i++)for(let j=i+1;j<units.length;j++){if(units[i].el.contains(units[j].el)||units[j].el.contains(units[i].el))continue;if(ov(units[i].b,units[j].b))res.push('LABELxLABEL: '+units[i].t+' | '+units[j].t)}
const icons=[...svg.querySelectorAll('g[transform^="translate"]')].filter(g=>g.querySelector('path,rect')&&!g.querySelector('text'));
for(const u of units)for(const g of icons){if(ov(u.b,bb(g)))res.push('LABELxICON: '+u.t+' | '+g.getAttribute('transform'))}
for(let i=0;i<icons.length;i++)for(let j=i+1;j<icons.length;j++){if(ov(bb(icons[i]),bb(icons[j])))res.push('ICONxICON: '+icons[i].getAttribute('transform')+' | '+icons[j].getAttribute('transform'))}
const important=c=>['#8a2f1f','#9fbcc0','#2a2118','#3d3566'].includes(c);
const out={};
for(const g of svg.querySelectorAll('line,polyline,circle,path,ellipse')){if(g.closest('defs'))continue;if(g.closest('g[transform^="translate"]'))continue;
 const stroke=g.getAttribute('stroke')||'';const fill=g.getAttribute('fill')||'';
 if(g.tagName==='circle'&&fill&&fill!=='none'&&+g.getAttribute('r')>100)continue;
 if(g.dataset && g.dataset.skip)continue;
 const inClip=!!g.closest('[clip-path]');
 let L;try{L=g.getTotalLength()}catch(e){continue}
 const m=g.getCTM();const step=Math.max(1.5,L/4000);
 for(let s=0;s<=L;s+=step){const p=g.getPointAtLength(s);const q=svg.createSVGPoint();q.x=p.x;q.y=p.y;const r=q.matrixTransform(m);
  if(inClip&&!(r.x>clipR.x0&&r.x<clipR.x1&&r.y>clipR.y0&&r.y<clipR.y1))continue;
  for(const u of units){if(u.el.contains(g)||g.parentNode.contains(u.el)&&g.parentNode!==svg&&!g.closest('[clip-path]'))continue;const b=u.b;if(r.x>b.x0+1&&r.x<b.x1-1&&r.y>b.y0+1.5&&r.y<b.y1-1){
    if(u.plated&&!important(stroke)&&!(g.tagName==='circle'&&+g.getAttribute('r')<12))continue;
    const k=u.t+' ⟂ '+g.tagName+'['+(stroke||fill)+']';out[k]=(out[k]||0)+1}}}}
return res.concat(Object.entries(out).map(([k,v])=>v+'  '+k)).join('\n');
})()
