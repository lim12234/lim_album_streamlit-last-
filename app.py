import streamlit as st

st.set_page_config(
    page_title="나만의 웹 갤러리",
    page_icon="./images/gallery.png"
)

st.markdown("""
<style>
img {
	max-height: 300px;
}
h1 {
    color: #FA8072;
} 
h3 {
    color: #C8A2C8;
}           
                       
.stTextLabelWrapper div {
    display: flex;
    justify-content: center;
    font-size: 16px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
[data-testid="StyledFullScreenButton"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title("*추억을 남기는 나만의 앨범")
st.subheader("사진을 등록하고 당신의 추억을 남겨보세요!")

type_emoji_dict = {
    "인물": "",
    "풍경": "",
    "여행": "",
    "식물": "",
    "동물": "",
    "음식": "",
    "거리": "",
    "스포츠": "",
    "연예인": "",
    "기타": ""
}

init_pictures = [
    {
        "name": "얼굴천재 - 차은우",
        "types": ["연예인", "인물"],
        "year": "2023",
        "image_url": "https://i.namu.wiki/i/a369iTUZpZ4mQMu7kcv2mNW74uxw5dTBoN6Yp3VQWDNQBV-WaZpOWhqaB3MKARSldDefujTT2cGVbDpY4Dmw9eF9m2A4E32s9ETwS13s-dWDKW_aKAHUx8c6gaIBYsz8P0FsRW5yVeIzUOSvfVeFsw.webp"
    },
    {
        "name": "반려묘 - 레오",
        "types": ["동물"],
        "year": "2021",
        "image_url": "https://i.namu.wiki/i/f9wIM4uooxiYPe2BXd8Arc48awTTpHbqVojE9tdA-4tfE7BaTNNnCQlnIoCfEF6GHnRjDjBWcNav7L6Hc8YFGfC_Cz4n-rbC23oyKEIbQWzSJ8lM4QsPEDq4gLUy0hv1KkkljGDibUTEB0lmyXBlsw.webp"
    },
    {
        "name": "가족 여행 - 몰디브 바다",
        "types": ["풍경", "여행"],
        "year": "2019",
        "image_url": "https://i.namu.wiki/i/IZ5eaTO4N-8at0IOFy-DRCRJj8Mo1DhCP7WA7eDnpbpHD3AJBZbuUlrm8KHXuQQd6Mt1PDXiD3te2COgzRBzuZJoMwxg7-girFl71HnvsaQn7Fxb5LkWYQ_-iuwhWRKKWS3gokmRaNw595QCKqtOUQ.webp"
    },
    {
        "name": "내가 만든 파스타",
        "types": ["음식"],
        "year": "2022",
        "image_url": "https://i.namu.wiki/i/sgJsljPJQjQFUYA8BkbtrZtuqlrCeAbcD-nNCSIXUh7pg2Soxh_FsDcsHlz6I72JnmwATzb2WJIF8WcC-OCQzZhHqTGciwdhnYvLAHUmiF7AAKBLKz5UHCAAvy3unuaI1SUZt11seDa8nr2Z-Hlm8w.webp"
    },
]

if "pictures" not in st.session_state:
    st.session_state.pictures = init_pictures

example_picture = {
    "name": "모리 코고로",
    "types": ["인물"],
    "year": "2000",
    "image_url": "https://i.namu.wiki/i/n4bYabT6tNKTyp4UiDkX3J2VzKTrxvY1OJsfXn7LiCICDs-WFCkkQzyZerb6Yvnn4GZzUbYfb6fODTmIr97R0LIKONecnq0asHvUT-qpdok3pb50plN3bQntB_Ui0-ZzSVDYsHFM4g1uJyd1bESlFQ.webp"
}

auto_complete = st.toggle("예시 사진 정보로 채우기")
with st.form(key="form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input(
            label="사진 이름",
            value=example_picture["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="사진 종류",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_picture["types"] if auto_complete else []
        )
    with col3:
        year = st.text_input(
            label="사진 촬영 연도",
            value=example_picture["year"] if auto_complete else ""
        )

    image_url = st.text_input(
        label="사진 URL 정보",
        value=example_picture["image_url"] if auto_complete else ""
        )
    submit = st.form_submit_button(label="내 앨범에 추가하기")
    if submit:
        if not name:
            st.error("사진의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("사진의 종류를 적어도 한 개 선택해주세요.")
        elif not year:
            st.error("사진의 연도를 입력해주세요.")
        else:
            st.success("사진을 추가할 수 있습니다.")
            st.session_state.pictures.append({
                "name": name,
                "types": types,
                "year": year,
                "image_url": image_url if image_url else "./images/default.png"
            })


for i in range(0, len(st.session_state.pictures), 2):
    row_pictures = st.session_state.pictures[i:i+2]
    cols = st.columns(2)
    for j in range(len(row_pictures)):
        with cols[j]:
            picture = row_pictures[j]
            with st.expander(label=f"**{i+j+1}. {picture['name']: <10}, {picture['year']}**", expanded=True):
                st.image(picture["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in picture["types"]]
                st.text(" /".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.pictures[i+j]
                    st.rerun()