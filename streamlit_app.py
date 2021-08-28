from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import multiprocessing
import numpy as np


a  = np.random.rand(3,1000)

df = pd.DataFrame(a.head())

st.write(df)
#st.set_config('browser.uiDirection', 'RTL')  # defaults to 'LTR'


# st.markdown("""
# <style>
# input {
#   unicode-bidi:bidi-override;
#   direction: RTL;
# }
# </style>
#     """, unsafe_allow_html=True)

# st.markdown("""
# <style>
# input, .rtl {
#   unicode-bidi:bidi-override;
#   direction: RTL;
# }
# </style>
#     """, unsafe_allow_html=True)

# text = st.text_input("text input")

# st.markdown('<div class="rtl">%s</div>' % text, unsafe_allow_html=True)
# # st.write()
# st.markdown(
#     """
#     <style>
#     p, div, input, label {
#     unicode-bidi:bidi-override;
#     direction: RTL;
#     text-align: right;
#     }
#     </style>
#     <link href="//db.onlinewebfonts.com/c/6b75b24d502dab23003320c2e1b2fc68?family=Adobe+Arabic" rel="stylesheet" type="text/css"/>
#     <style> bdi {font-family: 'Adobe Arabic';}</style>

#     <p><bdi>ویلیام صوری (۱۱۳۰ – ۲۹ سپتامبر ۱۱۸۶ میلادی) اسقف اعظم و تاریخ‌نگار قرون وسطایی بود. او در اورشلیم در دروان اوج پادشاهی اورشلیم، که در سال ۱۰۹۹ و پس از نخستین جنگ صلیبی پایه‌گذاری شده‌بود، رشد و پرورش یافت و بیست سال از عمرش را صرف مطالعهٔ علوم مقدماتی و الهیات در مدرسه پاریس و بولونیا کرد. درپی بازگشت ویلیام به اورشلیم در سال ۱۱۶۵، پادشاه اِمالریک او را به عنوان سفیر به امپراتوری بیزانس فرستاد. بعدها ویلیام به آموزگاری پسر پادشاه منصوب شد که در آینده با نام بالدوین چهارم به تخت نشست. همچنین او بود که بیماری جذام بالدوین را شناسایی کرد. پس از مرگ امالریک، ویلیام بدل به کنسول و اسقف اعظم صور شد، که جایگاه این دو رتبه از میان بلندرتبه‌ترین‌ منصب‌های اداری پادشاهی اورشلیم محسوب می‌شدند. او همچنین در سال ۱۱۷۹ و در سومین شورای لاتْران به نمایندگی شرق لاتین برگزیده شد. از آنجایی که او از افراد درگیر در کشمکش‌های سیاسی دوران پادشاهی بالدوین چهارم به حساب می‌آمد، اهمیت و جایگاهش با قدرت یافتن دستهٔ رقیب در امور سلطنتی، رو به کاهش نهاد. او در جرگهٔ افراد با اعتبار اورشلیم به حساب می‌آمد و احتمالاً در سال ۱۱۸۶ درگذشت. او امروزه به‌عنوان مورخ پادشاهی اورشلیم، یکی از بزرگترین وقایع‌نامه‌نویسان جنگ‌های صلیبی و یکی از بزرگترین وقایع‌نویسان قرون وسطی در اروپا شناخته می‌شود. وقایع‌نامه وی، با عنوانی همچون هیستوریا رِروم اینْ پارتیبوس گِشتاروم، هیستوریا ایروزولیمیتانا (تاریخ اورشلیم) و عنوان مختصر هیستوریا شناخته می‌شود. این اثر مشهور ویلیام، پس از مرگ به‌سرعت به زبان فرانسوی و پس از آن به زبان‌های دیگر ترجمه شد؛ چرا که اثر وی، تنها منبع کامل و جامع در رابطه با قرن ۱۲ اورشلیم است که توسط یک بومی نوشته شده‌است.</bdi></p>
#     """,
#     unsafe_allow_html=False,)

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.write(f"Number of cores : {multiprocessing.cpu_count()}")

#so how to do it?

# with st.echo(code_location='below'):
total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

Point = namedtuple('Point', 'x y')
data = []

points_per_turn = total_points / num_turns

for curr_point_num in range(total_points):
    curr_turn, i = divmod(curr_point_num, points_per_turn)
    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    radius = curr_point_num / total_points
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    data.append(Point(x, y))

st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    .mark_circle(color='#0068c9', opacity=0.5)
    .encode(x='x:Q', y='y:Q'))
