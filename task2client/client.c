int main(){
    int fd;

    fd = open("dev/foo", O_RDONLY);
    while(1) {
        unsigned int t;
        read(fd, &t, sizeof(t));
        cout << t << endl;
    }
}