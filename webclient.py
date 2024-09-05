import socket
import sys

if __name__ == "__main__":

    if len(sys.argv) == 3 :
        address = (sys.argv[1], int(sys.argv[2]))
    else:
        address = (sys.argv[1], 80)

    client = socket.socket()

    client.connect(address)

    #payload = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent elementum vestibulum elit, at accumsan felis placerat eget. Suspendisse vestibulum, eros nec suscipit efficitur, turpis risus placerat justo, nec venenatis diam nulla a orci. In laoreet rutrum mauris ut euismod. In dignissim nisl ac felis pellentesque, sed venenatis purus aliquam. Integer at tristique ante, quis dictum est. Phasellus sed lorem varius, finibus nibh eu, fermentum urna. Suspendisse potenti. Nunc sed purus enim. Aliquam erat volutpat. Sed aliquam orci lacus, ac tincidunt nibh fermentum sed. Praesent efficitur rhoncus urna, a cursus justo gravida ac. Nam ullamcorper tellus eget ex tristique, in suscipit metus tempus. In hendrerit libero sit amet dolor lobortis, et vehicula ex facilisis.\nPellentesque at massa suscipit, placerat metus tempus, imperdiet nunc. Nulla facilisi. Sed consectetur ligula ut metus dictum consectetur. Vestibulum luctus nisi et quam iaculis, vitae pulvinar lacus pharetra. Nullam in sodales ex. Quisque nec nulla interdum ex semper ornare. Nullam sed lorem lacinia, feugiat magna vitae, sodales lacus. Praesent vel libero ante. Vestibulum sit amet erat fermentum odio luctus laoreet vitae ac diam. Sed efficitur nisi porttitor erat lacinia elementum. Donec interdum massa nunc, a dictum lacus malesuada sit amet. Phasellus pellentesque, elit eu mollis congue, nunc est pretium lectus, id euismod lacus metus ut elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos\nMorbi pulvinar odio ante, ut tempus eros vehicula a. Donec a sollicitudin lectus. Nam nibh dui, blandit egestas ligula ut, mattis placerat velit. In vitae tincidunt ligula. Donec pretium a nisl vitae blandit. Donec congue ullamcorper velit, quis tempor erat ultricies eget. Sed pulvinar sit amet massa vel rhoncus. Etiam malesuada, neque vel ullamcorper venenatis, ex ante suscipit sapien, vel tincidunt orci mauris quis dolor. Donec commodo sagittis ante, eu porttitor nisi dapibus vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec ornare felis eget magna volutpat, ut sagittis velit convallis. Curabitur consectetur mauris erat, sodales aliquam tortor porta ac. Praesent interdum non erat eu ornare\nUt vulputate convallis ex hendrerit finibus. Nam eu malesuada metus, at fringilla est. Aliquam accumsan ex erat, id molestie diam tristique dignissim. Maecenas imperdiet bibendum magna vel condimentum. Aliquam pretium ornare orci sed volutpat. Cras accumsan at justo quis mollis. Fusce aliquet tellus eget ligula malesuada sagittis. Proin nibh sem, sollicitudin sed velit quis, bibendum euismod est. Integer sit amet accumsan nunc. Suspendisse arcu ligula, gravida commodo velit vel, fermentum fermentum massa. Sed tempus finibus lacus eget faucibus.\nMaecenas eu vulputate nisi. Etiam pharetra odio in enim sollicitudin, sit amet egestas odio interdum. Etiam placerat, elit tristique condimentum tempus, quam quam facilisis magna, eget faucibus nulla lectus commodo felis. Mauris in risus quis massa accumsan vulputate sit amet nec tellus. Praesent commodo porta nisi, ut vestibulum eros porta ac. Curabitur sed magna ligula. Ut ac scelerisque enim. Ut euismod tincidunt dictum. Curabitur id interdum sem. Pellentesque ac libero finibus, sodales dui at, rhoncus quam. Nulla elementum congue dolor, ut hendrerit arcu lobortis nec. \nPellentesque ut vehicula ligula. Sed a neque eu metus sagittis rhoncus. Etiam porttitor eget sapien non pellentesque. Mauris euismod augue enim, sed rutrum enim bibendum vel. Nunc rutrum egestas lectus aliquet varius. Cras dapibus tempor sem, vitae rutrum ex vehicula quis. Curabitur quis elit sed felis tempor varius eu bibendum velit. Ut rhoncus faucibus nisi quis aliquet. \nNam blandit arcu at varius rhoncus. Nullam felis nisl, consectetur sed consequat in, sodales nec erat. Nulla vel turpis vel tortor imperdiet ultricies. Proin sed nisi vitae lacus tincidunt bibendum et at justo. Aenean nisl orci, ullamcorper ut massa ut, dictum ultrices nulla. Sed pulvinar nisi vitae interdum facilisis. Phasellus iaculis ipsum tellus, eu hendrerit enim auctor at. Proin ac vehicula odio. Curabitur sodales libero augue, non porttitor sem bibendum quis. Praesent maximus imperdiet varius. Aliquam vehicula, elit quis dapibus laoreet, nibh ligula consectetur tortor, sit amet pretium metus arcu vitae velit. Vivamus sit amet euismod arcu.\nCurabitur mattis vel quam ac porttitor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum in ex ante. Sed interdum faucibus arcu quis fermentum. Vestibulum ultricies molestie bibendum. Aenean sit amet arcu id tellus luctus vestibulum. Nullam gravida sollicitudin bibendum. Cras malesuada dapibus leo, ac bibendum est ultricies ac. Ut lectus nisl, ultrices a purus et, varius dictum lectus. \nMaecenas et lacus nisl. Fusce id massa nec turpis mollis facilisis. Nulla efficitur feugiat tellus sit amet convallis. Morbi vitae sapien dolor. Quisque dictum diam magna, in condimentum dolor condimentum ultrices. Donec porta pharetra purus vitae facilisis. Donec ut viverra lorem. Nunc commodo, velit id aliquet cursus, magna leo ultrices tellus, vel luctus tellus tortor eget libero. Duis sagittis tempus tellus. Curabitur quis sodales nulla. Vivamus sit amet vulputate libero. Pellentesque vitae dolor euismod, molestie mauris ac, dictum ligula. Duis sagittis risus nibh, sed sagittis lectus volutpat eget. Suspendisse rutrum quam ipsum, vitae interdum augue malesuada sit amet. Quisque sed purus convallis tortor convallis auctor. \nCras lectus mauris, ullamcorper in convallis id, sodales in lacus. Phasellus lacus velit, fermentum vel pulvinar nec, pretium tincidunt mi. Quisque tristique iaculis egestas. Duis fringilla, lectus id ultricies tincidunt, nulla eros tincidunt massa, quis pellentesque turpis ex et justo. Duis iaculis orci ex, nec facilisis leo interdum et. Nam aliquam aliquam nec"
    payload = "test payloadÿ"
    #payload = ""
    contentLenght = "Content Length: " + str(len(payload))
    contentType = "text/plain"
    request = "GET /dsf HTTP/1.1\r\nHost: %s\r\n%s\r\n%s\r\nConnection: close\r\n\r\n%s" % (sys.argv[1], contentType, contentLenght, payload)

    print(request)

    client.sendall(request.encode("ISO-8859-1"))

    response = b''
    while True:
        buffer = client.recv(4096)
        if not buffer:
            break
        response += buffer
    response = response.decode("ISO-8859-1")
    client.close()
    
    print(response)