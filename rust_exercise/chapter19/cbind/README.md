# 如何在C中调用Rust代码

# 1.  Rust Project Setup

- 通过Cargo new  —lib参数创建一个Rust 项目。
- Cargo.toml文件中指定生成库文件。

```rust
[lib]
name = "your_crate"
crate-type = ["staticlib"]  # Creates static lib
#crate-type = ["cdylib"]      # Creates dynamic lib
```

- 构建C API代码

**# [no_mangle]**

Rust编译器处理符号名称的方式与c语言链接器期望的方式不同。因此，需要告知Rust编译器不要对要在Rust之外使用的任何函数进行改动。

**extern“ C”**

默认情况下，您在Rust中编写的任何函数都将使用Rust ABI(它也是不稳定的)。而当构建FFI API时，我们需要告诉编译器使用系统ABI。根据您的平台，您可能要特定的ABI版本，这些在[此处](https://doc.rust-lang.org/reference/items/external-blocks.html)中进行了说明。

```rust
#[no_mangle]
pub extern "C" fn call_from_c() {
    println!("Just called a Rust function from C!");
}
```

# 2.  生成C头文件

通过‣ 自动执行，可以分析Rust代码，然后从中生成C和C++项目的头文件。

铜鼓如下命令安装cbindgen。

`cargo install --force cbindgen`

如下命令导出c的头文件。`cbindgen.toml` 可以为空。

`cbindgen --config cbindgen.toml --crate my_rust_library --output my_header.h —lang c`

# 编写一个C程序并且开始编译

编写一个简单的C文件作为测试用例。代码如下：

```rust
#include "stdio.h"
#include "my_header.h"
int main() {
    printf("C executed form here..\n");
    call_from_c();
    return 0;
}
```

编译C文件

`gcc -c main.c`
拷贝Rust 库文件到当前目录下,然后用如下的命令生成可执行文件

`gcc -o <execute_file> <my_rust_library> main.o`

这样就大工告成。输出结果如下

`C executed form here..
Just called a Rust function from C!`

# 参考文档

[https://stevenbai.top/rustbook/book/interoperability/rust-with-c.html](https://stevenbai.top/rustbook/book/interoperability/rust-with-c.html)

[https://github.com/eqrion/cbindgen](https://github.com/eqrion/cbindgen)
