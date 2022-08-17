use std::ops::Deref;

fn main() {
    let x = 5;
    let y = &x;

    assert_eq!(5, x);
    assert_eq!(5, *y);

    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);

    struct Mybox<T>(T);
    impl<T> Mybox<T> {
        fn new(x: T) -> Mybox<T> {
            Mybox(x)
        }
    }
    impl<T> Deref for Mybox<T> {
        type Target = T;
        fn deref(&self) -> &Self::Target {
            &self.0
        }
    }

    let x = 5;
    let y = Mybox::new(x);
    assert_eq!(5, x);
    assert_eq!(5, *y);

    let m = Mybox::new(String::from("Rust"));
    hello(&m);

    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
    println!("CustomSmartPointers created.");
    drop(c);
}

fn hello(name: &str) {
    println!("Hello, {name}!");
}

struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Dropping CustomSmartPointer with data `{}`!", self.data);
    }
}
