from pykakasi import kakasi
import streamlit as st
import urllib
import json

kks = kakasi()
url = "http://www.google.com/transliterate?"

st.title("パワー系回文Bot🤖")
st.write(f"パワー系回文とは：https://dic.nicovideo.jp/a/うょしん部のコカ様〜 ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("入力してください"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    prompt = prompt.replace("\n","").replace(" ","").replace("　","")
    param = {"langpair":"ja-Hira|ja","text":prompt[::-1]}
    paramstr = urllib.parse.urlencode(param)
    res = urllib.request.urlopen(url+paramstr)
    data = json.loads(res.read())
    response = prompt + "".join([d[1][0] for d in data])
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})