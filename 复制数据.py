import os
import shutil

# 源路径与目标路径
src_root = r"C:\Users\Administrator\Desktop\BS-RSC\BS-RSC\test"
dst_root = r"C:\Users\Administrator\Desktop\RS-GS"

# 遍历 Scene1 到 Scene50
for i in range(51, 66):
    scene_name = f"Scene{i}"
    dst_subfolder = f"{i-1:03d}"  # 生成 000 到 049

    for mode in ['RS', 'GS']:
        src_dir = os.path.join(src_root, scene_name, mode)
        dst_dir = os.path.join(dst_root, mode, dst_subfolder)

        os.makedirs(dst_dir, exist_ok=True)  # 如果目标文件夹不存在就创建

        # 遍历复制文件
        for file_name in os.listdir(src_dir):
            src_file = os.path.join(src_dir, file_name)
            dst_file = os.path.join(dst_dir, file_name)

            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)  # 支持替换已有文件

print("图片复制完成 ✅")
