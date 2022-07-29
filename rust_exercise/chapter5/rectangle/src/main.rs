#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        if (self.width >= other.width && self.height >= other.height) ||
            (self.width >= other.height && self.height >= other.width) {
            return true;
        } else {
            return false;
        }
    }
}

fn main() {

    let rect1 = Rectangle{width: 2, height: 3};
    let rect2 = Rectangle{width: 20, height: 30};
    let rect3 = Rectangle{width: 40, height: 20};
    println!("rect1 is {:#?}", rect1);
    println!("area of rect1 is {}", rect1.area());

    dbg!(&rect1);

    if rect3.can_hold(&rect1) {
        println!("rect3 can hold rect1");
    } else {
        println!("rect3 can not hold rect1");
    }

    if rect3.can_hold(&rect2) {
        println!("rect3 can hold rect2");
    } else {
        println!("rect3 can not hold rect2");
    }
}
