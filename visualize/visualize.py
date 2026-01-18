import matplotlib.pyplot as plt

def animate(grid, start, target, algo_path, algo_visited_order, algo_name="Algorithm"):
    plt.figure()

    plt.imshow(grid, cmap="gray_r")
    plt.title(f"{algo_name.upper()} Robot Ortami (Grid)")
    plt.xticks(range(grid.shape[1]))
    plt.yticks(range(grid.shape[0]))
    plt.grid(True)

    # Start (yeşil)
    plt.scatter(start[1], start[0], c="green", s=150, label="Start")

    # Target (kırmızı) sabit duruyor.
    plt.scatter(target[1], target[0], c="red", s=150, label="Target")


    plt.ion()  # İnteraktif mod açılır, Grafik bloklamaz yani  Kod çalışmaya devam eder,  Grafik anlık güncellenebilir, Gerçek zamanlı grafik ve animasyon için kullanılır. Animasyon sürekli devam etmez döngün ne zaman biterse animasyonda biter

    # Ziyaret edilen hücreler
    for pos in algo_visited_order[1:]:
        if pos == target:
            break

        plt.scatter(pos[1], pos[0], c="lightgray", s=80)
        plt.pause(0.03)


    robot = None  # robotun bulunduğu konumu sürekli değiştrerek tutacak
    
    for pos in algo_path[1:]:

        plt.scatter(pos[1], pos[0], c="lightblue", s=120) # robotun geçtiği hücreyi açık mavi boya (kalıcı)

        if robot: # Eğer bu koşul eklenmeseydi her geçtiği yerde iz bırakırdı
            robot.remove() 

        
        robot = plt.scatter(pos[1], pos[0], c="blue", s=150, label = f"{algo_name.upper()} Robot") # Robot (mavi) , yani mavi nokta sürekli robot_plot değişkenine atılıyor
        plt.pause(0.35)  # t saniye bekler,  Bu sürede: grafik yenilenir, pencere donmaz. plt.pause(0.1) =>  0.1 saniye dur + grafiği günceller. Neden time.sleep() değil dersen çünkü bunu kullanırsan → pencere donar. Ama plt.pause()'da donmaz

        

    plt.ioff() # plt.ioff() 'da kod durur. Açılan interaktif mod kapanır. Animasyon / simülasyon bittiğinde, son grafiği sabit bırakmak istediğinde programı kontrollu kapatmak için kullanılır.
    plt.legend()
    plt.show()