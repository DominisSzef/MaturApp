(function() {
    const BACKEND = 'http://localhost:8080/api/chat/ask';

    const style = document.createElement('style');
    style.textContent = `
    #matur-chat-btn {
      position: fixed; bottom: 28px; right: 28px;
      width: 58px; height: 58px; border-radius: 50%;
      background: linear-gradient(135deg, #0d6efd, #6610f2);
      border: none; cursor: pointer;
      box-shadow: 0 4px 20px rgba(13,110,253,0.5);
      z-index: 9999; display: flex; align-items: center;
      justify-content: center; transition: transform 0.2s, box-shadow 0.2s;
      color: white; font-size: 24px;
    }
    #matur-chat-btn:hover { transform: scale(1.1); box-shadow: 0 6px 28px rgba(13,110,253,0.7); }
    #matur-chat-btn .badge-dot {
      position: absolute; top: 4px; right: 4px;
      width: 12px; height: 12px; background: #00ff88;
      border-radius: 50%; border: 2px solid #000;
      animation: pulse-dot 2s infinite;
    }
    @keyframes pulse-dot { 0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.6;transform:scale(0.8);} }
    #matur-chat-box {
      position: fixed; bottom: 100px; right: 28px;
      width: 360px; max-height: 520px;
      background: #111; border: 1px solid #333; border-radius: 20px;
      z-index: 9998; display: none; flex-direction: column;
      box-shadow: 0 12px 48px rgba(0,0,0,0.8); overflow: hidden;
    }
    #matur-chat-box.open { display: flex; animation: slideUp 0.25s ease; }
    @keyframes slideUp { from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);} }
    #matur-chat-header {
      background: linear-gradient(135deg, #0d6efd, #6610f2);
      padding: 14px 18px; display: flex; align-items: center; gap: 10px;
    }
    .chat-avatar { width:36px;height:36px;background:rgba(255,255,255,0.2);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px; }
    .chat-hinfo { flex:1; }
    .chat-hname { font-weight:700;color:white;font-size:14px; }
    .chat-hstatus { font-size:11px;color:rgba(255,255,255,0.75); }
    #matur-chat-close { background:rgba(255,255,255,0.15);border:none;color:white;width:28px;height:28px;border-radius:50%;cursor:pointer;font-size:14px;display:flex;align-items:center;justify-content:center;transition:background 0.2s; }
    #matur-chat-close:hover { background:rgba(255,255,255,0.3); }
    #matur-chat-messages { flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;max-height:340px;scrollbar-width:thin;scrollbar-color:#333 transparent; }
    .chat-msg { max-width:82%;padding:10px 14px;border-radius:16px;font-size:13.5px;line-height:1.5;animation:msgIn 0.2s ease; }
    @keyframes msgIn { from{opacity:0;transform:translateY(6px);}to{opacity:1;transform:translateY(0);} }
    .chat-msg.bot { background:#1e1e2e;color:#e0e0ff;border-bottom-left-radius:4px;align-self:flex-start;border:1px solid #2a2a3e; }
    .chat-msg.user { background:linear-gradient(135deg,#0d6efd,#6610f2);color:white;border-bottom-right-radius:4px;align-self:flex-end; }
    .typing-dots span { display:inline-block;width:6px;height:6px;background:#666;border-radius:50%;margin:0 2px;animation:bounce 1.2s infinite; }
    .typing-dots span:nth-child(2){animation-delay:0.2s;}.typing-dots span:nth-child(3){animation-delay:0.4s;}
    @keyframes bounce { 0%,80%,100%{transform:translateY(0);}40%{transform:translateY(-6px);} }
    .chat-suggestions { display:flex;flex-wrap:wrap;gap:6px;padding:0 16px 12px; }
    .chat-sugg-btn { background:#1e1e2e;border:1px solid #333;color:#aaa;border-radius:12px;padding:5px 12px;font-size:12px;cursor:pointer;transition:all 0.2s;white-space:nowrap; }
    .chat-sugg-btn:hover { background:#0d6efd22;border-color:#0d6efd;color:#7eb3ff; }
    #matur-chat-footer { padding:12px 14px;border-top:1px solid #222;display:flex;gap:8px;align-items:center;background:#0a0a0a; }
    #matur-chat-input { flex:1;background:#1a1a1a;border:1px solid #333;border-radius:20px;padding:10px 16px;color:white;font-size:13px;outline:none;transition:border-color 0.2s; }
    #matur-chat-input:focus { border-color:#0d6efd; }
    #matur-chat-input::placeholder { color:#555; }
    #matur-chat-send { width:38px;height:38px;background:linear-gradient(135deg,#0d6efd,#6610f2);border:none;border-radius:50%;color:white;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;transition:transform 0.15s,opacity 0.2s;flex-shrink:0; }
    #matur-chat-send:hover{transform:scale(1.1);}
    #matur-chat-send:disabled{opacity:0.4;cursor:default;transform:none;}
    @media(max-width:480px){#matur-chat-box{width:calc(100vw - 32px);right:16px;bottom:90px;}#matur-chat-btn{right:16px;bottom:16px;}}
  `;
    document.head.appendChild(style);

    const wrap = document.createElement('div');
    wrap.innerHTML = `
    <button id="matur-chat-btn" title="Zapytaj MaturBota">🤖<span class="badge-dot"></span></button>
    <div id="matur-chat-box">
      <div id="matur-chat-header">
        <div class="chat-avatar">🤖</div>
        <div class="chat-hinfo"><div class="chat-hname">MaturBot</div><div class="chat-hstatus">● Asystent matematyczny</div></div>
        <button id="matur-chat-close">✕</button>
      </div>
      <div id="matur-chat-messages"></div>
      <div class="chat-suggestions" id="chat-suggestions">
        <button class="chat-sugg-btn">Co to logarytm?</button>
        <button class="chat-sugg-btn">Jak liczyc delte?</button>
        <button class="chat-sugg-btn">Wzory trygonometryczne</button>
        <button class="chat-sugg-btn">Ciag geometryczny</button>
      </div>
      <div id="matur-chat-footer">
        <input id="matur-chat-input" type="text" placeholder="Zapytaj o matematyke..." maxlength="500"/>
        <button id="matur-chat-send">&#10148;</button>
      </div>
    </div>
  `;
    document.body.appendChild(wrap);

    const messages = [];
    let isLoading = false;
    const box = document.getElementById('matur-chat-box');
    const input = document.getElementById('matur-chat-input');
    const sendBtn = document.getElementById('matur-chat-send');
    const msgsDiv = document.getElementById('matur-chat-messages');
    const sugDiv = document.getElementById('chat-suggestions');

    addMsg('bot', 'Czesc! Jestem MaturBot. Zapytaj mnie o cokolwiek z matematyki maturalnej!');

    document.getElementById('matur-chat-btn').addEventListener('click', toggle);
    document.getElementById('matur-chat-close').addEventListener('click', toggle);
    input.addEventListener('keydown', e => { if(e.key==='Enter') send(); });
    sendBtn.addEventListener('click', send);
    sugDiv.querySelectorAll('.chat-sugg-btn').forEach(b => {
        b.addEventListener('click', () => { input.value = b.textContent; sugDiv.style.display='none'; send(); });
    });

    function toggle() {
        const open = box.classList.toggle('open');
        document.getElementById('matur-chat-btn').style.transform = open ? 'scale(0.9)' : '';
        if(open) { input.focus(); msgsDiv.scrollTop = msgsDiv.scrollHeight; }
    }

    function addMsg(role, text) {
        const d = document.createElement('div');
        d.className = 'chat-msg ' + role;
        d.innerHTML = text.replace(/\n/g,'<br>');
        msgsDiv.appendChild(d);
        msgsDiv.scrollTop = msgsDiv.scrollHeight;
    }

    async function send() {
        const text = input.value.trim();
        if(!text || isLoading) return;
        input.value = '';
        sugDiv.style.display = 'none';
        addMsg('user', text);
        messages.push({role:'user', content:text});
        isLoading = true; sendBtn.disabled = true;

        const typing = document.createElement('div');
        typing.className = 'chat-msg bot';
        typing.innerHTML = '<span class="typing-dots"><span></span><span></span><span></span></span>';
        msgsDiv.appendChild(typing);
        msgsDiv.scrollTop = msgsDiv.scrollHeight;

        try {
            const res = await fetch(BACKEND, {
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({messages})
            });
            typing.remove();
            if(res.ok) {
                const data = await res.json();
                messages.push({role:'assistant', content:data.reply});
                addMsg('bot', data.reply);
            } else {
                addMsg('bot', 'Blad serwera. Sprobuj ponownie.');
            }
        } catch(e) {
            typing.remove();
            addMsg('bot', 'Brak polaczenia z serwerem.');
        }
        isLoading = false; sendBtn.disabled = false; input.focus();
    }
})();