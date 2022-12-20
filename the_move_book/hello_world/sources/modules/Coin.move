// modules/hello_world.move
address 0x2 {
module Coin {

    friend 0x02::Example;

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

        let _x = (1u64 as u8);

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

