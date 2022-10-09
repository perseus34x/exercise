use std::rc::Rc;
use std::thread;

fn main() {

    let num1 = Rc::new(1);
    let num2 = Rc::new(2);
    let num3 = Rc::new(3);
    let closure = {
        // `num1` is moved
        let num2 = num2.clone();  // `num2` is cloned
        let num3 = num3.as_ref();  // `num3` is borrowed
        move || {
            *num1 + *num2 + *num3
        }
    };
    println!("closuere is {:?}", closure());

    let num4 = 4;
    let num5 =5;
    let _closure1 = {
        let ret = move || {
            num4 + num5
        };
        ret();
        println!("num4 is {}", num4);
    };
    println!("num4 is {}", num4);

    thread::spawn(move || {println!("num5 is {}", num5)})
           .join()
           .unwrap();
    println!("num5 is {}", num5);
}
