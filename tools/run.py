# -*- coding: utf-8 -*-

import speedtest

s = speedtest.Speedtest()
s.get_best_server()
s.download()
download_speed = s.results.download / 1000000

new_cafe_file = open('../new_cafe.geojson', 'w')
new_cafe_file.writelines(
    [
        ',\n',
        '    {\n',
        '      "type": "Feature",\n',
        '      "properties": {\n',
        '        "名称": "",\n',
        '        "下载速度": "{0:.2f} Mbps",\n'.format(download_speed),
        '        "Speedtest 链接": "",\n',
        '        "评论 (@)": "",\n',
        '        "厕所": "",\n'
    ]
)
if (download_speed > 10):
    new_cafe_file.write(
        '        "marker-color": "#50C240",\n'
    )
elif (download_speed > 4):
    new_cafe_file.write(
        '        "marker-color": "#F3AE1A",\n'
    )
else:
    new_cafe_file.write(
        '        "marker-color": "#C24740",\n'
    )
new_cafe_file.writelines(
    [
        '        "marker-symbol": "cafe"\n',
        '      },\n',
        '      "geometry": {\n',
        '        "type": "Point",\n',
        '        "coordinates": [\n'
    ]
)
new_cafe_file.close()
