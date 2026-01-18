import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import patheffects
from matplotlib.lines import Line2D  # <-- Bunu eklememiz gerekiyor (Açıklama kutusu için)

def animate_bellman_ford(grid, start, target, path, visited_order, total_cost):
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#1E1E1E')
    
    ROWS, COLS = grid.shape
    ax.set_xlim(-0.5, COLS - 0.5)
    ax.set_ylim(ROWS - 0.5, -0.5)
    ax.set_facecolor('#263238')

    ax.set_xticks([])  # X eksenindeki sayıları kapatır
    ax.set_yticks([])  # Y eksenindeki sayıları kapatır


    # --- Yeni Renk Tanımlamaları ---
    COLOR_WALL   = '#37474F'   # Bina/Engel (-1)
    COLOR_FREE   = "#0F833F"   # Akıcı (Maliyet 1) -> Normal Yeşil
    COLOR_BELES  = '#58FF33'   # BELEŞ YOL (Maliyet 0) -> Parlak/Açık Yeşil
    COLOR_MED    = '#F1C40F'   # Orta (Maliyet 3) -> Sarı
    COLOR_HIGH   = '#E74C3C'   # Yoğun (Maliyet 6) -> Kırmızı
    
    def is_road(r, c):
        if 0 <= r < ROWS and 0 <= c < COLS:
            return grid[r, c] != -1
        return False

    for r in range(ROWS):
        for c in range(COLS):
            val = grid[r, c]
            
            if val == -1:
                ax.add_patch(patches.Rectangle((c-0.5, r-0.5), 1, 1, color='#151515', zorder=1))
                ax.add_patch(patches.Rectangle((c-0.45, r-0.45), 0.9, 0.9, color=COLOR_WALL, zorder=2))
            else:
                # Renk Seçimi
                if val == 0: 
                    road_color = COLOR_BELES
                elif val == 1: 
                    road_color = COLOR_FREE
                elif val == 3: 
                    road_color = COLOR_MED
                elif val >= 6: 
                    road_color = COLOR_HIGH
                else:
                    road_color = COLOR_FREE
                
                ax.add_patch(patches.Circle((c, r), 0.18, color=road_color, zorder=3, alpha=0.8))

                w = 14 
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    if is_road(r + dr, c + dc):
                        ax.plot([c, c + dc*0.5], [r, r + dr*0.5], color=road_color, linewidth=w, zorder=3)
                        ax.plot([c, c + dc*0.5], [r, r + dr*0.5], color='white', lw=1, ls='--', alpha=0.2, zorder=4)

    ax.scatter(target[1], target[0], c='#FF00FF', s=550, marker='*', edgecolors='white', zorder=25)
    robot = ax.scatter(start[1], start[0], c='#00B0FF', s=350, edgecolors='white', linewidth=2, zorder=30)

    # --- BAŞLIKLARI ÖNCEDEN OLUŞTUR (Hata Almamak İçin) ---
    # Sabit kısım (Beyaz)
    fixed_text = ax.text(COLS/2 - 0.5, -1.2, "Bellman-Ford Algoritması: ", color='white', 
                         fontsize=11, fontweight='bold', ha='right', va='center')
    # Dinamik kısım (Rengi değişecek olan)
    status_text = ax.text(COLS/2 - 0.4, -1.2, "Hazırlanıyor...", color='white', 
                          fontsize=11, fontweight='bold', ha='left', va='center')
    
    # --- YENİ: Toplam Maliyet Yazısı (Başlangıçta boş) ---
    cost_text = ax.text(COLS/2, -0.7, "", color='white', 
                        fontsize=11, ha='right', va='bottom', fontweight='bold')

    # --- HAREKET ANİMASYONU ---
    if path:
        for i in range(len(path)):
            r, c = path[i]
            val = grid[r, c]
            robot.set_offsets([c, r])
            
            if i > 0:
                pr, pc = path[i-1]
                ax.plot([pc, c], [pr, r], color='white', linewidth=3, zorder=20,
                        path_effects=[patheffects.withStroke(linewidth=6, foreground='black')])

            # Başlık Güncelleme (Hatasız Yöntem)
            if (r, c) == target:
                status_text.set_text("Hedefe Varıldı ✓")
                status_text.set_color(COLOR_BELES) # Yeşil
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
        Line2D([0], [0], marker='o', color='w', label='Beleş Yol (0)', markerfacecolor=COLOR_BELES, markersize=10),
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