script {
    use Std::Debug::print;
    use Std::Vector;
    use 0x2::Coin;
 
    fun burn() {
        let coin = Coin::mint(100);
        print(&Coin::modify_value(&mut coin));
        print(&Coin::value(&coin));
        Coin::burn(coin);

        let v = Vector::empty<u64>();
        Vector::push_back(&mut v, 5);
        Vector::push_back(&mut v, 6);
        print(&v);

        let _y = (1u64 as u8);
    }
}