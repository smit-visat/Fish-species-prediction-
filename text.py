import re

# The input string with package details
package_info = """
blinker @ file:///C:/b/abs_d9y2dm7cw2/croot/blinker_1696539752170/work
Bottleneck @ file:///C:/b/abs_f05kqh7yvj/croot/bottleneck_1707864273291/work
Brotli @ file:///C:/b/abs_3d36mno480/croot/brotli-split_1714483178642/work
certifi @ file:///C:/b/abs_7bbxxprxir/croot/certifi_1720453609121/work/certifi
charset-normalizer @ file:///croot/charset-normalizer_1721748349566/work
click @ file:///C:/b/abs_f9ihnt72pu/croot/click_1698129847492/work
colorama @ file:///C:/b/abs_a9ozq0l032/croot/colorama_1672387194846/work
Flask @ file:///C:/b/abs_f9w7doyu0h/croot/flask_1716545924884/work
gunicorn==22.0.0
idna @ file:///C:/b/abs_aad84bnnw5/croot/idna_1714398896795/work
importlib-metadata @ file:///C:/b/abs_c1egths604/croot/importlib_metadata-suite_1704813568388/work
itsdangerous @ file:///C:/b/abs_c4vwgdr5yn/croot/itsdangerous_1716533399914/work
Jinja2 @ file:///C:/b/abs_92fccttino/croot/jinja2_1716993447201/work
joblib @ file:///C:/b/abs_f4b98l6lgk/croot/joblib_1718217224240/work
MarkupSafe @ file:///C:/b/abs_ecfdqh67b_/croot/markupsafe_1704206030535/work
mkl-fft @ file:///C:/b/abs_19i1y8ykas/croot/mkl_fft_1695058226480/work
mkl-random @ file:///C:/b/abs_edwkj1_o69/croot/mkl_random_1695059866750/work
mkl-service==2.4.0
numexpr @ file:///C:/b/abs_afm0oewmmt/croot/numexpr_1683221839116/work
numpy @ file:///C:/Users/dev-admin/mkl/numpy_and_numpy_base_1682982345978/work
packaging @ file:///C:/b/abs_c3vlh0z4jw/croot/packaging_1720101866539/work
pandas @ file:///C:/miniconda3/conda-bld/pandas_1692299636855/work
platformdirs @ file:///C:/b/abs_b6z_yqw_ii/croot/platformdirs_1692205479426/work
pooch @ file:///C:/b/abs_a8nmng7d_x/croot/pooch_1695850149827/work
PySocks @ file:///C:/ci/pysocks_1605287845585/work
python-dateutil @ file:///C:/b/abs_3au_koqnbs/croot/python-dateutil_1716495777160/work
pytz @ file:///C:/b/abs_6ap4tsz1ox/croot/pytz_1713974360290/work
requests @ file:///C:/b/abs_9frifg92q2/croot/requests_1721410901096/work
scikit-learn @ file:///C:/b/abs_daon7wm2p4/croot/scikit-learn_1694788586973/work
scipy==1.10.1
six @ file:///tmp/build/80754af9/six_1644875935023/work
threadpoolctl @ file:///C:/b/abs_def0dwqlft/croot/threadpoolctl_1719407816649/work
tzdata @ file:///croot/python-tzdata_1690578112552/work
urllib3 @ file:///C:/b/abs_a7hvzm4y95/croot/urllib3_1718912661242/work
Werkzeug @ file:///C:/b/abs_8bittcw9jr/croot/werkzeug_1716533366070/work
win-inet-pton @ file:///C:/ci/win_inet_pton_1605306167264/work
zipp @ file:///C:/b/abs_b0beoc27oa/croot/zipp_1704206963359/work
"""

# Define a regex pattern to match packages with versions
pattern = r"([a-zA-Z0-9\-]+)(==| @ file:\/\/\/)[^\/]*"

# Find all matches using regex
matches = re.findall(pattern, package_info)

# Print the results
for match in matches:
    package_name = match[0]
    version_info = match[1]
    version = version_info.split('==')[1] if '==' in version_info else 'unknown'
    print(f"{package_name}: {version}")
