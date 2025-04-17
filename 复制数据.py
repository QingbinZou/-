import os
import shutil

# ====== 配置区域 ======
src_root = r"C:\Users\Administrator\Desktop\BS-RSC\BS-RSC\test"  # 源根目录
dst_root = r"C:\Users\Administrator\Desktop\RS-GS"              # 目标根目录

scene_start = 51   # 起始 Scene 编号，例如 Scene51
scene_end = 65     # 结束 Scene 编号，例如 Scene65
dst_start = 50     # 映射到的目标文件夹编号起始，例如从000到049之后，这里是050
# =====================

for i in range(scene_start, scene_end + 1):
    scene_name = f"Scene{i}"
    dst_subfolder = f"{dst_start + (i - scene_start):03d}"  # 映射为050到064

    for mode in ['RS', 'GS']:
        src_dir = os.path.join(src_root, scene_name, mode)
        dst_dir = os.path.join(dst_root, mode, dst_subfolder)

        os.makedirs(dst_dir, exist_ok=True)

        for file_name in os.listdir(src_dir):
            src_file = os.path.join(src_dir, file_name)
            dst_file = os.path.join(dst_dir, file_name)

            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)

print("✅ 图片复制完成")
