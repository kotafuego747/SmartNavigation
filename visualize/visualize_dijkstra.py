import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import patheffects 
from matplotlib.lines import Line2D 

def animate_dijkstra(grid, start, target, path, visited_order, total_cost):
    plt.ion()
    # Koyu modern tema
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#1E1E1E')
    
    ROWS, COLS = grid.shape
    ax.set_xlim(-0.5, COLS - 0.5)
    ax.set_ylim(ROWS - 0.5, -0.5)
    ax.set_facecolor('#263238') # Harita tabanı

    # --- Renk Tanımlamaları ---
    COLOR_WALL = '#37474F'   # Bina/Engel
    COLOR_FREE = '#2ECC71'   # Akıcı (Yeşil)
    COLOR_MED  = '#F1C40F'   # Orta (Sarı)
    COLOR_HIGH = '#E74C3C'   # Yoğun (Kırmızı)
    
    def is_road(r, c):
        if 0 <= r < ROWS and 0 <= c < COLS:
            return grid[r, c] != -1
        return False

    # 1. HARİTA VE YOL AĞINI OLUŞTUR
    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r, c]
            if val == -1:
                # Binaları çiz
                ax.add_patch(patches.Rectangle((c-0.5, r-0.5), 1, 1, color='#151515', zorder=1))
                ax.add_patch(patches.Rectangle((c-0.45, r-0.45), 0.9, 0.9, color=COLOR_WALL, zorder=2))
            else:
                # Yol zeminini trafik rengine göre boya
                if val == 1: road_color = COLOR_FREE
                elif val == 3: road_color = COLOR_MED
                elif val == 6: road_color = COLOR_HIGH
                
                ax.add_patch(patches.Circle((c, r), 0.2, color=road_color, zorder=3))

                # Komşularla yolları birleştir (Kıvrımlı yol yapısı)
                w = 15 # Yol genişliği
                if is_road(r-1, c): # Yukarı
                    ax.plot([c, c], [r, r-0.5], color=road_color, linewidth=w, zorder=3)
                    ax.plot([c, c], [r, r-0.5], color='white', lw=1, ls='--', alpha=0.3, zorder=4)
                if is_road(r+1, c): # Aşağı
                    ax.plot([c, c], [r, r+0.5], color=road_color, linewidth=w, zorder=3)
                    ax.plot([c, c], [r, r+0.5], color='white', lw=1, ls='--', alpha=0.3, zorder=4)
                if is_road(r, c-1): # Sol
                    ax.plot([c, c-0.5], [r, r], color=road_color, linewidth=w, zorder=3)
                    ax.plot([c, c-0.5], [r, r], color='white', lw=1, ls='--', alpha=0.3, zorder=4)
                if is_road(r, c+1): # Sağ
                    ax.plot([c, c+0.5], [r, r], color=road_color, linewidth=w, zorder=3)
                    ax.plot([c, c+0.5], [r, r], color='white', lw=1, ls='--', alpha=0.3, zorder=4)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    # Hedef Yıldızı
    ax.scatter(target[1], target[0], c='#FF00FF', s=500, marker='*', edgecolors='white', zorder=25)

    # Robotu Başlat
    robot = ax.scatter(start[1], start[0], c='#00B0FF', s=350, edgecolors='white', linewidth=2, zorder=30)

    fixed_text = ax.text(COLS/2 - 0.5, -1.2, "Dijkstra Algoritması: ", color='white', 
                         fontsize=11, fontweight='bold', ha='right', va='center')
    # Dinamik kısım (Rengi değişecek olan)
    status_text = ax.text(COLS/2 - 0.4, -1.2, "Hazırlanıyor...", color='white', 
                          fontsize=11, fontweight='bold', ha='left', va='center')
    
    # --- YENİ: Toplam Maliyet Yazısı (Başlangıçta boş) ---
    cost_text = ax.text(COLS/2, -0.7, "", color='white', 
                        fontsize=11, ha='right', va='bottom', fontweight='bold')


    # 2. ANİMASYON DÖNGÜSÜ
    if path:
        for i in range(len(path)):
            r, c = path[i]
            val = grid[r, c]
            # Robotun konumunu güncelle
            robot.set_offsets([c, r])
            
            # Arkasında beyaz-siyah belirgin iz bırak
            if i > 0:
                pr, pc = path[i-1]
                ax.plot([pc, c], [pr, r], color='white', linewidth=4, zorder=20,
                        path_effects=[patheffects.withStroke(linewidth=7, foreground='black')])

            # Başlık Güncelleme (Hatasız Yöntem)
            if (r, c) == target:
                status_text.set_text("Hedefe Varıldı ✓")
                status_text.set_color(COLOR_FREE) # Yeşil
                cost_text.set_text(f"Toplam Yol Maliyeti: {total_cost}")
            else:
                status_text.set_text("Robot İlerliyor...")
                status_text.set_color("white") # Beyaz
            
            plt.pause(0.04 if val == 0 else 0.1)
    else:
        status_text.set_text("Hedefe Varılamadı X")
        status_text.set_color(COLOR_HIGH) # Kırmızı




    # --- 4. GELİŞMİŞ AÇIKLAMA KUTUSU (LEGEND) ---
    legend_elements = [
        # Mevcut Renkler
        Line2D([0], [0], marker='o', color='w', label='Akıcı Yol (1)', markerfacecolor=COLOR_FREE, markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Orta Yol (3)', markerfacecolor=COLOR_MED, markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Yoğun Yol (6)', markerfacecolor=COLOR_HIGH, markersize=10),
        
        # Yeni Eklenenler (Robot, Hedef, Rota, Engel)
        Line2D([0], [0], marker='o', color='w', label='Robot', markerfacecolor='#00B0FF', markersize=10), # Mavi Robot
        Line2D([0], [0], marker='*', color='w', label='Hedef', markerfacecolor='#FF00FF', markersize=14), # Pembe Yıldız
        Line2D([0], [0], color='white', lw=2, label='Rota'), # Beyaz Çizgi
        Line2D([0], [0], marker='s', color='w', label='Engel', markerfacecolor=COLOR_WALL, markersize=10),
    ]

    leg = ax.legend(handles=legend_elements, 
                    loc='lower center', 
                    bbox_to_anchor=(0.5, -0.08), # Konumu ayarladık
                    ncol=4,  # 4 sütun yaptık (Böylece 2 satır halinde şık duracak)
                    frameon=False, 
                    fontsize=9)
    
    plt.setp(leg.get_texts(), color='white')
    
    plt.ioff()
    plt.show()





























