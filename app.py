import streamlit as st, random, time
st.set_page_config(page_title="VocaNova AI",page_icon="✦",layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Manrope:wght@600;800&display=swap');
.stApp{background:radial-gradient(ellipse at top right,#4b1830,#170f15 55%);color:#fff4f8}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
.block-container{max-width:1100px;padding-top:2rem}
h1,h2,h3{font-family:Manrope,sans-serif}
.hero{font-family:Manrope,sans-serif;font-size:3.4rem;font-weight:800;line-height:1.08}
.pink{color:#ff4f91}.muted{color:#cbbbc4}
.panel{background:linear-gradient(135deg,#421b2d,#21151d);border:1px solid #633049;border-radius:20px;padding:1.4rem}
.stat{background:#21151d;border:1px solid #633049;border-radius:15px;padding:1rem}
div.stButton>button{background:linear-gradient(120deg,#8b2149,#5a1735);color:white;border:1px solid #a83b65;border-radius:12px;font-weight:700;min-height:2.5rem}
[data-testid="stSidebar"]{background:#170f15}
</style>""",unsafe_allow_html=True)
WORDS={
"A1":[("apple","алма","an apple a day","I eat an apple every morning."),("borrow","қарызға алу","borrow a book","Can I borrow your pen?"),("friendly","мейірімді","a friendly person","Our neighbour is friendly."),("usually","әдетте","usually do","I usually walk to class."),("choose","таңдау","choose a colour","You can choose your favourite colour.")],
"A2":[("advice","кеңес","give advice","My teacher gave me useful advice."),("comfortable","ыңғайлы","feel comfortable","These shoes are comfortable."),("experience","тәжірибе","gain experience","I want to gain experience."),("healthy","дені сау","a healthy lifestyle","Sleep is part of a healthy lifestyle."),("prepare","дайындау","prepare for an exam","I need to prepare for my exam.")],
"B1":[("achieve","қол жеткізу","achieve a goal","Small steps help you achieve your goals."),("confident","өзіне сенімді","feel confident","Practice makes me feel confident."),("opportunity","мүмкіндік","a great opportunity","This course is a great opportunity."),("solution","шешім","find a solution","Let's find a solution together."),("support","қолдау","offer support","Friends can offer support.")],
"B2":[("accurate","дәл","accurate information","Please use accurate information."),("beneficial","пайдалы","highly beneficial","Reading is highly beneficial."),("effective","тиімді","an effective method","Feedback is an effective method."),("maintain","сақтау","maintain progress","Practice helps maintain progress."),("significant","елеулі","a significant change","We noticed a significant change.")],
"C1":[("ambiguous","екіұшты","an ambiguous statement","The instructions were ambiguous."),("compelling","нанымды","a compelling argument","She presented a compelling argument."),("facilitate","жеңілдету","facilitate learning","Games can facilitate learning."),("inevitable","сөзсіз","an inevitable result","Some change is inevitable."),("substantial","елеулі","substantial progress","She made substantial progress.")],
"C2":[("alleviate","жеңілдету","alleviate pressure","A break can alleviate pressure."),("discern","ажыратып тану","discern a pattern","Researchers discerned a pattern."),("eloquent","шешен","an eloquent speaker","He is an eloquent speaker."),("nuanced","нәзік айырмашылықтары бар","a nuanced view","The issue needs a nuanced view."),("scrutinize","мұқият тексеру","scrutinize the evidence","We must scrutinize the evidence.")]}
LEVELS=list(WORDS)
if "saved" not in st.session_state: st.session_state.saved=[]
if "completed" not in st.session_state: st.session_state.completed=[]
if "chat" not in st.session_state: st.session_state.chat=[]
if "idx" not in st.session_state: st.session_state.idx=0
page=st.sidebar.radio("✦ VOCANOVA AI",["Home","Learn vocabulary","Topic test","AI Coach","My progress","About the project"])
st.sidebar.markdown("---")
st.sidebar.caption("Your vocabulary, your journey.")
st.sidebar.caption("Created by Madina Sabirova")
if page=="Home":
 st.markdown('<div class="muted">A SMARTER WAY TO LEARN ENGLISH</div><div class="hero">Words that stay.<br><span class="pink">Confidence that grows.</span></div><p class="muted">Build real vocabulary through context, practice, and a learning journey designed around you.</p>',unsafe_allow_html=True)
 a,b=st.columns([1.2,1])
 with a:
  st.markdown('<div class="panel"><h2>Make today count.</h2><p class="muted">Learn useful words, see them in real-life phrases, then test what you remember. Every small session moves you forward.</p></div>',unsafe_allow_html=True)
 with b:
  st.markdown('<div class="panel"><h3>Your learning path</h3><p>A1 → A2 → B1 → B2 → C1 → C2</p><p class="muted">Choose a level that fits your goals and keep moving.</p></div>',unsafe_allow_html=True)
 st.write("")
 c=st.columns(3)
 for col,title,val in zip(c,["WORDS SAVED","TOPICS COMPLETED","TARGET LEVEL"],[len(st.session_state.saved),len(st.session_state.completed),"B2"]):
  col.markdown(f'<div class="stat"><div class="muted">{title}</div><h2>{val}</h2></div>',unsafe_allow_html=True)
 st.markdown('<p style="text-align:center;margin-top:3rem" class="muted">Created by <b class="pink">Madina Sabirova</b></p>',unsafe_allow_html=True)
elif page=="Learn vocabulary":
 st.title("Vocabulary Studio")
 level=st.selectbox("CEFR level",LEVELS)
 words=WORDS[level]; i=st.session_state.idx%len(words); w,tr,phrase,example=words[i]
 st.markdown(f'<div class="panel"><div class="muted">{level} · VOCABULARY CARD</div><h1 style="font-size:3rem">{w}</h1><h3 class="pink">{tr}</h3><hr><div class="muted">USEFUL COLLOCATION</div><h3>{phrase}</h3><div class="muted">IN CONTEXT</div><p>{example}</p></div>',unsafe_allow_html=True)
 c=st.columns(3)
 if c[0].button("← Previous"): st.session_state.idx=(i-1)%len(words); st.rerun()
 if c[1].button("♡ Save word"):
  if w not in st.session_state.saved: st.session_state.saved.append(w)
  st.toast("Word saved!")
 if c[2].button("Next word →"): st.session_state.idx=(i+1)%len(words); st.rerun()
 st.caption("Pronunciation audio can be connected in a later version.")
elif page=="Topic test":
 st.title("Topic test")
 st.caption("5 questions · 90 seconds · Any wrong answer restarts the test.")
 level=st.selectbox("Choose level",LEVELS,key="testlevel")
 if "quiz" not in st.session_state or st.session_state.get("quizlevel")!=level:
  if st.button("Start test"):
   st.session_state.quiz=random.sample(WORDS[level],min(5,len(WORDS[level]))); st.session_state.qi=0; st.session_state.quizlevel=level; st.session_state.started=time.time(); st.rerun()
 elif st.session_state.qi<len(st.session_state.quiz):
  remaining=max(0,90-int(time.time()-st.session_state.started))
  st.markdown(f'<div class="stat"><h2>{remaining}s remaining</h2><p>Question {st.session_state.qi+1} of 5</p></div>',unsafe_allow_html=True)
  w,tr,_,_=st.session_state.quiz[st.session_state.qi]
  st.subheader(f"What does **{w}** mean?")
  options=[tr]+[x[1] for x in WORDS[level] if x[1]!=tr]
  random.shuffle(options); answer=st.radio("Select translation",options,key=f"q{st.session_state.qi}")
  if st.button("Check answer"):
   if answer==tr:
    st.session_state.qi+=1
    if st.session_state.qi>=len(st.session_state.quiz): st.session_state.completed.append(level)
    st.rerun()
   else:
    st.error(f"Correct answer: {tr}. Restarting from the beginning.")
    st.session_state.pop("quiz"); st.session_state.pop("quizlevel"); st.rerun()
 else:
  st.success("Excellent! You completed the test.")
  if st.button("Try again"): st.session_state.pop("quiz",None); st.session_state.pop("quizlevel",None); st.rerun()
elif page=="AI Coach":
 st.title("AI Coach")
 st.markdown('<div class="panel"><p class="muted">Practise English naturally. Live AI replies require a securely configured OpenAI API key in the hosting platform Secrets settings. Never share your key publicly.</p></div>',unsafe_allow_html=True)
 for m in st.session_state.chat:
  with st.chat_message(m["role"]): st.write(m["content"])
 prompt=st.chat_input("Write a message in English…")
 if prompt:
  st.session_state.chat.append({"role":"user","content":prompt})
  try:
   from openai import OpenAI
   key=st.secrets["OPENAI_API_KEY"]
   client=OpenAI(api_key=key)
   msgs=[{"role":"system","content":"You are VocaNova AI, a warm English vocabulary coach. Respond naturally to the learner's message, ask a relevant follow-up question, and gently correct one important English mistake. Keep it concise and encouraging."}]+st.session_state.chat[-10:]
   reply=client.chat.completions.create(model="gpt-4o-mini",messages=msgs).choices[0].message.content
  except Exception:
   reply="Thanks for practising! Can you tell me one more detail? Try to use a new English word in your answer. Live personalized replies need the site's owner to configure an API key securely."
  st.session_state.chat.append({"role":"assistant","content":reply}); st.rerun()
elif page=="My progress":
 st.title("My progress")
 a,b,c=st.columns(3)
 a.metric("Words saved",len(st.session_state.saved)); b.metric("Topics completed",len(st.session_state.completed)); c.metric("Goal level","B2")
 st.subheader("Learning journey")
 for level in LEVELS: st.write(("✦ " if level=="A1" else "○ ")+level)
 st.subheader("Saved words")
 st.write(", ".join(st.session_state.saved) if st.session_state.saved else "Save words from Vocabulary Studio to see them here.")
 st.subheader("Personal profile")
 name=st.text_input("Your name","Madina")
 start=st.selectbox("Current level",LEVELS)
 goal=st.selectbox("Target level",LEVELS,index=3)
 st.caption(f"{name}: {start} → {goal}")
elif page=="About the project":
 st.title("About VocaNova AI")
 st.markdown('<div class="panel"><h3>Research project</h3><p class="muted">The Effectiveness of AI Chatbots in Improving EFL Learners’ Vocabulary Knowledge.</p><p>VocaNova combines CEFR vocabulary cards, collocations, example sentences, retrieval practice, progress tracking, and AI conversation coaching.</p><h3>Prototype limitations</h3><p class="muted">Progress is currently session-based. Shared accounts, leaderboard, push notifications, and cloud-synced progress require further development. Live AI coaching requires a secure API key and may incur API charges.</p></div>',unsafe_allow_html=True)
 st.markdown('<p style="text-align:center;margin-top:2rem" class="muted">Created by <b class="pink">Madina Sabirova</b></p>',unsafe_allow_html=True)
