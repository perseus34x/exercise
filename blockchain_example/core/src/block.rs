use chrono::prelude::*;
use utils::coder;
use serde::{Serialize};

#[derive(Serialize, Debug)]
pub struct BlockHeader {
    pub time: i64,
    pub tx_hash: String, // transaction data merkel hash
    pub pre_hash: String,
}

#[derive(Debug)]
pub struct Block {
    pub header: BlockHeader,
    pub hash: String,
    pub data: String,  // transaction data
}

impl Block {
    pub fn new(data: String, pre_hash: String) -> Self {
        let tx_hash = coder::get_hash(&coder::my_serialize(&data));
        let time = Utc::now().timestamp(); 
        let mut block = Block {
            header: BlockHeader {
                time: time,
                tx_hash: tx_hash,
                pre_hash: pre_hash,
            },
            hash: String::from(""),
            data: data,
        };
        block.set_hash();
        block        
    }

    fn set_hash(&mut self) {
        let header = coder::my_serialize(&(self.header));
        self.hash = coder::get_hash(&header);
    }
}
