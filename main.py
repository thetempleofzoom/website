import streamlit as sl, pandas as pd


sl.title("The Best Company")
body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris rutrum egestas nunc id lobortis. Proin euismod vel ex vel ullamcorper. Proin viverra neque a elit volutpat malesuada. Maecenas faucibus, nulla vel dapibus cursus, nunc felis convallis velit, a scelerisque enim odio quis ligula. Sed viverra ullamcorper nibh, sit amet efficitur odio. Cras a bibendum lectus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ac eros ultrices, cursus erat sit amet, egestas diam."
sl.markdown(body)
sl.header("Our Team")

df = pd.read_csv('data.csv')
numcols = 3
numrowsdata = df.shape[0]
multiplier = int(numrowsdata/numcols)
cols = sl.columns(numcols)

for num in range(numcols):
    with cols[num]:
        for index, row in df[num*multiplier:(num+1)*multiplier].iterrows():
            sl.subheader(row['first name']+" "+row['last name'])
            sl.write(row['role'])
            sl.image("images/"+row['image'])
            sl.markdown("#")
