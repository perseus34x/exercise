// modules/hello_world.move
address 0x2 {
    module Coin {

        struct Coin has drop,copy {
            value: u64,
        }

        public fun mint(value: u64): Coin {
            Coin { value }
        }

        public fun value(coin: &Coin): u64 {
            coin.value
        }

        public fun burn(coin: Coin): u64 {
            let Coin { value } = coin;
            value
        }

        public fun modify_value(coin: &mut Coin): u64 {
            let c_ref = coin;
            // modify the refered value
            c_ref.value =150;

            // modify the value in the copied item
            let counterfeit = *c_ref;
            counterfeit.value = 200;
            counterfeit.value
        }
    }
}

address 0x8 {
    module Example {
        fun read_and_assign(store: &mut u64, new_value: &u64) {
            *store = *new_value
        }

        fun subtype_examples() {
            let x: &u64     = &mut 1;
            let y: &mut u64 = &mut 1;

            //x = &mut 1; // valid
            // y = &2; // invalid!

            read_and_assign(y, x); // valid
            //read_and_assign(x, y); // invalid!
        }
    }
}

address 0x9 {
    module Tuples {
        // all 3 of these functions are equivalent

        // when no return type is provided, it is assumed to be `()`
        fun returs_unit_1() { }

        // there is an implicit () value in empty expression blocks
        fun returs_unit_2(): () { }

        // explicit version of `returs_unit_1` and `returs_unit_2`
        fun returs_unit_3(): () { () }


        fun returns_3_values(): (u64, bool, address) {
            (0, false, @0x42)
        }
        fun returns_4_values(x: &u64): (&u64, u8, u128, vector<u8>) {
            (x, 0, 1, b"foobar")
        }
    }
}
address 0x10 {
    module Locals {

        use Std::Vector;
        struct S { f: u64, g: u64 }

        fun annotated() {
            let _u: u8 = 0;
            let _b: vector<u8> = b"hello";
            let _a: address = @0x0;
            let (_x, _y): (&u64, &mut u64) = (&0, &mut 1);
            let S { f: _f1, g: _f2 }: S = S { f: 0, g: 1 };

            let _v2: vector<u64> = Vector::empty(); // no error
        }
    }
}