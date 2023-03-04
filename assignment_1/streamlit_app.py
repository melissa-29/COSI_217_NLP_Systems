import streamlit as st
import pandas as pd
import plotly.express as px
from ner import get_entities_with_markup, get_entities
import json

def load_color_map(input_text: str) -> dict:
    with open(input_text, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

st.title('Named Entity Recognition via spaCy')
st.text("")
st.sidebar.markdown('# Named Entities found')

# Creates form and submit button for text input
with st.form(key='entity_form'):
    text_input = st.text_area("Enter some text to identify named entities:", height=200)
    submitted = st.form_submit_button('Get Entities')

if submitted:
    color_map = load_color_map("color_map.json")
    # When <entity class="PERSON">Sebastian Thrun</entity>
    markup = get_entities_with_markup(text_input)
    # (5, 20, 'PERSON', 'Sebastian Thrun')
    entities = get_entities(text_input)
    # {PERSON, NORP, ORG}
    entity_labels = set([entity[2] for entity in entities])

    # Create a dataframe with entity labels and their count
    entity_count_df = pd.DataFrame(columns=['Entity Label', 'Count'])

    # Populate sidebar
    for label in entity_labels:
        # 'Sebastian Thrun' if PERSON == label
        entity_mentions = [entity[3] for entity in entities if entity[2] == label]
        # 'Sebastian Thrun, Thrun'
        entity_mentions_str = ', '.join(entity_mentions)
        # PERSON(s): Sebastian Thrun, Thrun
        st.sidebar.write(f"<span style='border-bottom: 3px solid {color_map[label]['color']}'>{label}"
                         f" </span>(s): {entity_mentions_str}", unsafe_allow_html=True)

        entity_count_df = pd.concat([entity_count_df, pd.DataFrame(
            {'Entity Label': f"{label}",
             'Count': len([entity for entity in entities if entity[2] == label])}, index=[0])], ignore_index=True)

    # Display the dataframe in the sidebar
    # Apply styles to the DataFrame based on the given color map
    styled_df_html = entity_count_df.style.apply(lambda col:
                                                 ['color: %s' % color_map[val] if val in color_map else 'color: black'
                                                  for val in col] if col.name == 'Entity Label'
                                                 else [''] * len(col)).render()

    # Display the styled dataframe in the sidebar
    st.sidebar.markdown(styled_df_html, unsafe_allow_html=True)

    # Load CSS styles from file
    with open("static/css/st.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("""<hr style="height:3px; border:none; color:#333; background-color:#333; " /> """, unsafe_allow_html=True)
    st.subheader("Marked-up text:")
    st.markdown(f"<div class='marked-text'>{markup}</div>", unsafe_allow_html=True)
    st.text("")

    print(color_map)

    # Create a bar chart to visualize the entity counts
    fig = px.bar(entity_count_df, x='Entity Label', y='Count', color='Entity Label',
                 color_discrete_map={k: v['color'] for k, v in color_map.items()},
                 text=[color_map[label]['emoji'] for label in entity_count_df['Entity Label'].values.tolist()])
    fig.update_traces(textposition='outside')

    st.text("")
    st.subheader("Entities Count Bar Chart")
    st.plotly_chart(fig)

    st.balloons()
