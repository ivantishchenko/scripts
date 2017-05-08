package main

import (
    "fmt"
    "net/http"
    "strconv"
    "sync"
    "runtime"
    "io/ioutil"
)


const(
    URL = "http://ctf.slothparadise.com/about.php"
    N = 1000
)

func init() {
    runtime.GOMAXPROCS(runtime.NumCPU())
}

func main() {
    var wg sync.WaitGroup
    wg.Add(N)
    for i := 0; i < N; i++ {
        defer wg.Done()
        go func(ID int) {
            resp, err := http.Get(URL)
            if err != nil {
                fmt.Println("Reload" + strconv.Itoa(ID))
                body, _ := ioutil.ReadAll(resp.Body)
                bodyString := string(body)
                fmt.Println(bodyString)
            } else {
                fmt.Println("Error")
            }
        }(i)

    }
    wg.Wait()
}
