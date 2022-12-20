address 0x2 {
module Example {

    use 0x2::Coin;
    use Std::Debug::print;

    fun read_and_assign(store: &mut u64, new_value: &u64) {
        *store = *new_value
    }

    public fun subtype_examples() {
        let x: &u64     = &mut 1;
        let y: &mut u64 = &mut 1;

        //x = &mut 1; // valid
        // y = &2; // invalid!

        read_and_assign(y, x); // valid
        //read_and_assign(x, y); // invalid!


        let c = Coin::mint(300);
        let x = Coin::value(&c);
        print(&x);
        let _c = Coin::burn(c);

    }
}
}