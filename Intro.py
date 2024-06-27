import streamlit as st

st.markdown("# :orange[Hello!]")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown('''
    Welcome to my :red[streamlit] app where I am exploring some of its :blue-background[features].    
            On the sidebar, I have several mini projects that is showing :rainbow[different sets of skills with python and streamlit]:  
            ''')

st.html('''
<style>
    .intro-container {
            background-color: rgba(200,200,200,0.5);
        padding: 1rem;
        border-radius: 8px;
        
        }
    ol li h5 {
            margin-bottom: -8px
        }
    ol li p {padding-left: 12px;font-style:italic}        
</style>
        
        <div class="intro-container">
            <ol>
                <li><h5>Dummy Bank Analytics</h5> <p>A dummy dashboard where I analyze bank branches and created graph and table to look at their performace. You can look at the graph to look at branch actual performance vs target, and filter it by branch or look at all branches performance</p></li>
                <li><h5>Map</h5> <p>Map plotting of those branches using folium, with custom color on the pin based on branch performance</p></li>
                <li><h5>Movies</h5> <p>Learning how to use data from large CSV file and present it with python and streamlit. You can use the filter to see movie based on director</p></li>
                <li><h5>Calculator</h5> <p>A copy of Pixegami's work to learn on how to use streamlit. Here is the link to the <a href="https://www.youtube.com/watch?v=D0D4Pa22iG0&ab_channel=pixegami">video</a></p></li>
            </ol>
        </div>
''')