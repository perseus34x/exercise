// modules/hello_world.move
address 0x2 {
    module Coin {

        struct Coin has drop {
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

        public fun test() {
            let _a1 = @0x1;
            let _a2 = @0x2;
            // ... and so on for every other possible address
        }
    }
}
