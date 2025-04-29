from plyfile import PlyData

# 讀取 binary 格式的 PLY 檔案
ply = PlyData.read("ship_30K_point_cloud.ply")

# 顯示欄位名稱
print(ply['vertex'].data.dtype.names)

# 顯示第一筆資料
print(ply['vertex'].data[0])

# 將 binary 轉換為 ASCII 格式
ply.text = True
ply.write("ascii_version.ply")

print("Conversion to ASCII format completed.")