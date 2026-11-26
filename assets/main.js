/* Alchemist Mind Pros site scripts */
// ===== ONE PLACE TO SET YOUR BOOKING LINK =====
// Paste your Calendly event URL here (e.g. https://calendly.com/your-handle/strategy-call).
// Leave empty and every "Book" button scrolls to the booking section at the bottom of the page.
window.AMP_BOOKING_URL = window.AMP_BOOKING_URL || "https://calendly.com/tre-alchemistmind";

(function(){
  const $ = (s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];

  // Mobile menu
  const burger=$('.burger'), menu=$('.mobile-menu');
  if(burger&&menu){burger.addEventListener('click',()=>{const o=menu.classList.toggle('open');burger.setAttribute('aria-expanded',o)});
    $$('a',menu).forEach(a=>a.addEventListener('click',()=>menu.classList.remove('open')));}

  // Rotating H1
  $$('.rotator').forEach(r=>{
    const items=$$('span',r); if(items.length<2) return;
    let i=0; items[0].classList.add('on');
    setInterval(()=>{
      const cur=items[i]; i=(i+1)%items.length; const nxt=items[i];
      cur.classList.add('out'); cur.classList.remove('on');
      setTimeout(()=>cur.classList.remove('out'),500);
      nxt.classList.add('on');
    },3000);
  });

  // Reveal + bar animation
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');
    $$('.bar i[data-w]',e.target).forEach(b=>b.style.width=b.dataset.w);io.unobserve(e.target);}}),{threshold:.12});
  $$('.reveal, .dash, .mock').forEach(el=>io.observe(el));

  // Booking
  function openBooking(e){
    const url=window.AMP_BOOKING_URL;
    if(url && window.Calendly){e.preventDefault();window.Calendly.initPopupWidget({url});return;}
    if(url){return;} // falls through to href (set below)
    const t=$('#book'); if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'});}
  }
  if(window.AMP_BOOKING_URL){
    const l=document.createElement('link');l.rel='stylesheet';l.href='https://assets.calendly.com/assets/external/widget.css';document.head.appendChild(l);
    const s=document.createElement('script');s.src='https://assets.calendly.com/assets/external/widget.js';s.async=true;document.head.appendChild(s);
    $$('.js-book').forEach(a=>{a.href=window.AMP_BOOKING_URL;a.target='_blank';a.rel='noopener'});
  }
  $$('.js-book').forEach(a=>a.addEventListener('click',e=>{
    window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'book_click',location:a.dataset.loc||''});
    openBooking(e);
  }));

  // ===== Quiz =====
  const quiz=$('#quiz-app');
  if(quiz){
    const qs=$$('.q',quiz), total=qs.length, bar=$('.progress i',quiz), count=$('.qcount',quiz), back=$('.quiz-back',quiz), res=$('.result',quiz);
    const answers=[]; let idx=0;
    const gapsText=[
      "You can't see cost per signed case by channel, so budget decisions are based on lead volume, not revenue.",
      "Google and Meta aren't receiving signed-case outcomes, so the algorithms optimize for cheap leads instead of clients.",
      "Consult calls aren't being reviewed, so you can't tell whether low sign rates are a marketing or an intake problem.",
      "Paper check-in means re-keying data and losing the link between the ad that drove a client and the case they signed.",
      "Leads go cold without a trace, so you're paying for opportunities that leak out before the consult."
    ];
    function show(n){qs.forEach((q,i)=>q.classList.toggle('on',i===n));bar.style.width=(n/total*100)+'%';count.textContent=`Question ${n+1} of ${total}`;back.style.visibility=n?'visible':'hidden';}
    $$('.opt',quiz).forEach(b=>b.addEventListener('click',()=>{
      const qi=+b.closest('.q').dataset.i; answers[qi]=+b.dataset.v;
      if(qi<total-1){idx=qi+1;show(idx);} else finish();
    }));
    back.addEventListener('click',()=>{if(idx>0){idx--;show(idx);}});
    function finish(){
      qs.forEach(q=>q.classList.remove('on'));bar.style.width='100%';count.textContent='Your result';back.style.visibility='hidden';
      const score=Math.round(answers.reduce((a,b)=>a+b,0)/(total*2)*100);
      const tier= score>=80?{t:"Clear signal. You're ahead of most firms.",d:"Your foundation is strong. The next gains come from tightening the feedback loop so Google and Meta bid on your best case types, not just any case."}
              : score>=45?{t:"Partial visibility. You're leaving money on the table.",d:"You can see pieces of the picture, but the gaps below are where ad budget quietly leaks. Firms at this stage usually find 15 to 30% of spend that isn't producing signed cases."}
              :{t:"Flying blind. Your ads are optimizing for the wrong thing.",d:"Without signed-case data flowing back to your ad platforms, you're paying for leads, not clients. The good news: this is the fastest kind of problem to fix."};
      $('.score-num',res).textContent=score;
      const circ=2*Math.PI*64; const ring=$('.ring-fg',res); ring.style.strokeDasharray=circ; ring.style.strokeDashoffset=circ;
      requestAnimationFrame(()=>setTimeout(()=>{ring.style.transition='stroke-dashoffset 1.2s ease';ring.style.strokeDashoffset=circ*(1-score/100)},50));
      $('.res-title',res).textContent=tier.t; $('.res-desc',res).textContent=tier.d;
      const g=$('.gaps',res); g.innerHTML='';
      answers.forEach((v,i)=>{if(v<2){const d=document.createElement('div');d.className='gap';d.innerHTML=`<b>GAP ${String(i+1).padStart(2,'0')}</b><span>${gapsText[i]}</span>`;g.appendChild(d);}});
      res.classList.add('on');
      window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'quiz_complete',quiz_score:score});
    }
    $('.quiz-restart',quiz)?.addEventListener('click',()=>{answers.length=0;idx=0;res.classList.remove('on');show(0);});
    show(0);
  }

  // ===== Calculator =====
  $$('.calc').forEach(c=>{
    const inputs=$$('input[type=range]',c);
    const fmt=n=>'$'+Math.round(n).toLocaleString();
    function upd(){
      const v={};inputs.forEach(i=>{v[i.name]=+i.value;const p=(i.value-i.min)/(i.max-i.min)*100;i.style.setProperty('--p',p+'%');
        const o=c.querySelector(`output[for=${i.id}]`); if(o) o.textContent=i.dataset.fmt==='$'?fmt(i.value):(i.dataset.fmt==='%'?i.value+'%':(+i.value).toLocaleString());});
      const consults=v.leads*(v.show/100); const signed=consults*(v.close/100);
      const cpl=v.spend/Math.max(v.leads,1); const cpsc=signed>0?v.spend/signed:0;
      const waste=v.spend*0.2; const signedAfter=signed*1.0; // reallocated budget at same efficiency
      const cpscAfter=signed>0?(v.spend-waste)/signed:0;
      $('.o-cpsc',c).textContent=signed>0?fmt(cpsc):'n/a';
      $('.o-cpl',c).textContent=fmt(cpl);
      $('.o-signed',c).textContent=signed.toFixed(1);
      $('.o-consults',c).textContent=Math.round(consults);
      $('.o-yearly',c).textContent=fmt(waste*12);
      $('.o-after',c).textContent=signed>0?fmt(cpscAfter):'n/a';
    }
    inputs.forEach(i=>i.addEventListener('input',upd)); upd();
  });


  // ===== Phone video: autoplay muted, tap for sound, no pop-out =====
  const v=document.getElementById('amp-video'), sb=document.querySelector('.ph-sound'), pr=document.querySelector('.ph-progress i');
  if(v&&sb){
    const txt=sb.querySelector('.ps-txt');
    const io2=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ v.play().catch(()=>{}); } else if(v.muted){ v.pause(); } }),{threshold:.35});
    io2.observe(v);
    v.addEventListener('timeupdate',()=>{ if(pr&&v.duration) pr.style.width=(v.currentTime/v.duration*100)+'%'; });
    function toggle(){
      if(v.muted){ v.muted=false; v.loop=false; v.currentTime=0; v.play().catch(()=>{}); sb.classList.add('playing'); txt.textContent='Mute';
        window.dataLayer=window.dataLayer||[]; window.dataLayer.push({event:'video_sound_on',video:'what_we_do'}); }
      else { v.muted=true; v.loop=true; sb.classList.remove('playing'); txt.textContent='Tap for sound'; }
    }
    sb.addEventListener('click',toggle);
    v.addEventListener('click',()=>{ if(v.muted) toggle(); else if(v.paused) v.play(); else v.pause(); });
    v.addEventListener('ended',()=>{ v.muted=true; v.loop=true; v.play().catch(()=>{}); sb.classList.remove('playing'); txt.textContent='Watch again with sound';
      window.dataLayer=window.dataLayer||[]; window.dataLayer.push({event:'video_complete',video:'what_we_do'}); });
    v.addEventListener('contextmenu',e=>e.preventDefault());
  }
  // year
  $$('.yr').forEach(e=>e.textContent=new Date().getFullYear());
})();
