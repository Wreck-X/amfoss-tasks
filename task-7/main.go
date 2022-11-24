package main
import (
	"fmt"
	"syscall/js"
	. "github.com/siongui/godom/wasm"	
	
)
var Count = 0
func increment()js.Func{
		foo := Document.GetElementById("int")
	inc := js.FuncOf(func(this js.Value, args []js.Value) any {
		Count++
		foo.Set("innerHTML", fmt.Sprintf("%d", Count))
		return nil
	})
	return inc
}

func decrement()js.Func{
	foo := Document.GetElementById("int")
dec := js.FuncOf(func(this js.Value, args []js.Value) any {
	Count--
	foo.Set("innerHTML", fmt.Sprintf("%d", Count))
	return nil
})
return dec
}

func reset()js.Func{
	foo := Document.GetElementById("int")
res := js.FuncOf(func(this js.Value, args []js.Value) any {
	foo.Set("innerHTML", "0")
	Count = 0
	return nil
})
return res
}

var signal = make(chan int)

func keepAlive() {
      for {
              <-signal
      }
}


func main() {

	increm := Document.GetElementById("inc")
	increm.Call("addEventListener", "click", increment())
	decrem := Document.GetElementById("dec")
	decrem.Call("addEventListener", "click", decrement())
	reset_ := Document.GetElementById("res")
	reset_.Call("addEventListener", "click", reset())
	keepAlive()
}
