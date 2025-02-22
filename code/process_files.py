'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''

import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit
import json
from io import StringIO

st.title('Process Package Files')

if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'file_count' not in st.session_state:
    st.session_state.file_count = 0
if 'line_count' not in st.session_state:
    st.session_state.line_count = 0

file = st.file_uploader('Upload a package file')

if file:
    filename = file.name
    json_filename = filename.replace('.txt', '.json')
    packages = []
    text = StringIO(file.getvalue().decode('utf-8')).read()
    for line in text.split('\n'):
        line = line.strip()
        pkg = parse_packaging(line)
        total = calc_total_units(pkg)
        unit = get_unit(pkg)
        packages.append(pkg)
    package_count = len(packages)
    with open(f'./data/{json_filename}', 'w') as f:
        json.dump(packages, f, indent=4)
    summary = (f'{package_count} packages written to {json_filename}')
    st.session_state.file_count = st.session_state.file_count + 1
    st.session_state.line_count = st.session_state.line_count + 1
    st.session_state.summaries.append(summary)
    for s in st.session_state.summaries:
        st.info(s)
    st.success(f'{st.session_state.file_count} files and {st.session_state.line_count} lines processed')
