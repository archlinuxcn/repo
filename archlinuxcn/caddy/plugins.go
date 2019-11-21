package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"sort"
)

const URL = "https://caddyserver.com/v1/api/download-page"

type Plugin struct {
	Name       string
	ImportPath string
}
type PluginList struct {
	Plugins []Plugin `json:"plugins"`
}

func getPlugins() []Plugin {
	resp, err := http.Get(URL)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	list := PluginList{}
	err = json.Unmarshal(body, &list)
	if err != nil {
		log.Fatal(err)
	}
	return list.Plugins
}
func main() {
	plugins := getPlugins()
	sort.Slice(plugins, func(i, j int) bool {
		return plugins[i].Name < plugins[j].Name
	})
	if len(os.Args) == 1 {
		fmt.Println("plugins=(")
		for _, plugin := range plugins {
			fmt.Printf("#    '%s'\n", plugin.Name)
		}
		fmt.Println(")")
		return
	}
	pluginsMap := make(map[string]string)
	for _, plugin := range plugins {
		pluginsMap[plugin.Name] = plugin.ImportPath
	}
	for _, name := range os.Args[1:] {
		path, ok := pluginsMap[name]
		if !ok {
			log.Fatalf("cannot find plugin %s\n", name)
		}
		fmt.Printf(`_ "%s"`+"\n", path)
	}
}
