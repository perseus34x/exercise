script {
    use Std::Debug::print;
    use 0x6::Vecs;
    use Std::Vector;
    use 0x16::Structs;
    
    fun vec() {
        Vecs::mint(100);
        print(&b"Hello!");
        
        let v = Vector::empty<u8>();
        let v1 = Vector::singleton(1u8);
        // [debug] (&) [1]
        print(&v1);

        Vector::push_back(&mut v, 2u8);
        // [debug] (&) [2]
        print(&v);

        let v2 = Vector::borrow(&v1,0);
        // [debug] 1
        print(v2);

        let v3 = Vector::borrow_mut(&mut v, 0);
        *v3 = *v3 + 10;
        // [debug] 12
        print(v3);
        // [debug] (&) [12]
        print(&v);

        let v4 = Vector::borrow_mut(&mut v1, 0);
        // [debug] 1
        print(v4);

        Vector::append(&mut v, v1);
        // [debug] (&) [12, 1]
        print(&v);

        Vector::pop_back(&mut v1);
        Vector::destroy_empty(v1);

        let x = Vector::singleton<u64>(10);
        let _y = copy x;

        let _m: &u64 = &0;
        let _n: &mut u64 = &mut 1;

        _m = &mut 1; // valid
        _n = &mut 2; // invalid!

        let b: vector<u8> = b"Hello";
        print(Vector::borrow(&b, 2));

        let x = 0;
        x = x + 1;
        assert!(x == 1, 42);
        {
            x = x + 1;
            assert!(x == 2, 42);
        };
        assert!(x == 2, 42);

        Structs::read_write_fileds();
    }
}