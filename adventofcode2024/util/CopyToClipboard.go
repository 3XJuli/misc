package util

import (
	"fmt"

	"golang.design/x/clipboard"
)

// CopyToClipboard is for macOS
func CopyToClipboard(text string) error {

	err := clipboard.Init()

	if err != nil {
		return fmt.Errorf("error initializing clipboard: %w", err)
	}

	clipboard.Write(clipboard.FmtText, []byte(text))

	return nil
}
