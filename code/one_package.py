'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit

st.title('Process One Package')
package = st.text_input('Enter package data')
if package:
    parsed = parse_packaging(package)
    total_units = calc_total_units(parsed)
    unit = get_unit(parsed)
    st.text(parsed)
    for item in parsed:
        name = list(item.keys())[0]
        size = list(item.values())[0]
        st.info(f'{name} -> {size}')
    st.success(f'Total: {total_units} {unit}')
