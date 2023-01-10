import streamlit as st
import py3Dmol
from stmol import *
from stmol import showmol

st.title("Now lets look at the structure of the virus")

st.write("An analysis of the structural proteins of **African** and **Asian** strains of **Chikungunya virus**,\
 showed that both strains contain three structural proteins: **glycosylated E1 and E2**, embedded in the viral envelope, and a **nonglycosylated nucleocapsid protein**.")
st.write("These protein are still to be structurally characterized, but others one like \
    the **FHL1 protein**, which has be identified as a key cellular factor for the *replication and pathogenesis** of chikungunya is and can be seen:")
showmol(render_pdb(id = '2EGQ'))

st.write("We don't have the structure of the **chikungunya virus** (mainly because of the lack of fundings), but we can see the structure of the **Zika virus** which is similar on some points :")
showmol(render_pdb(id = '5IRE'))
#xyzview = py3Dmol.view(query='pdb:1A2C') 
#xyzview.setStyle({'cartoon':{'color':'spectrum'}})
#showmol(xyzview, height = 500,width=800)