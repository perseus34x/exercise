use bincode;
use serde::{Serialize, Deserialize};
use crypto::{digest::Digest, sha3::Sha3};

//pub fn my_serialize<T: ?Sized>(value: &T) -> Result<Vec<u8>>
//where
//    T: Serialize,
pub fn my_serialize<T: ?Sized>(value: &T) -> Vec<u8>
    where T: Serialize,
{
    bincode::serialize(value).unwrap()
}

// pub fn deserialize<'a, T>(bytes: &'a [u8]) -> Result<T>
// where
//    T: serde::de::Deserialize<'a>,
pub fn my_deserialize<'a, T>(bytes: &'a [u8]) -> T
where
    T: serde::de::Deserialize<'a>,
{
    bincode::deserialize(bytes).unwrap()
}

pub fn get_hash(value: &[u8]) -> String {
    let mut hasher = Sha3::sha3_256();
    hasher.input(value);
    hasher.result_str()
}

// unit test
#[derive(Serialize, Deserialize, PartialEq, Eq, Debug)]
pub struct Point {
    x: i32,
    y: i32,
}

#[cfg(test)]
mod tests {
    use crate::coder::Point;
    use crate::coder::{my_serialize, my_deserialize};

    #[test]
    fn coder_works() {
        let point = Point {x:1, y:1};
        let result:Point = my_deserialize(&my_serialize(&point));
        assert_eq!(point, result);
    }
}
