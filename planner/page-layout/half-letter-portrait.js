
//______________________________________________________________________
//______________________________________________________________________
//      _   __   _   _ _   _   _   _         _
// |   |_| | _  | | | V | | | | / |_/ |_| | /
// |__ | | |__| |_| |   | |_| | \ |   | | | \_
//  _  _         _ ___  _       _ ___   _                     / /
// /  | | |\ |  \   |  | / | | /   |   \                     (^^)
// \_ |_| | \| _/   |  | \ |_| \_  |  _/                     (____)o
//______________________________________________________________________
//______________________________________________________________________
//
//----------------------------------------------------------------------
// Copyright 2024, Rebecca Rashkin
// -------------------------------
// This code may be copied, redistributed, transformed, or built
// upon in any format for educational, non-commercial purposes.
//
// Please give me appropriate credit should you choose to use this
// resource. Thank you :)
//----------------------------------------------------------------------
//
//______________________________________________________________________
// //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
//______________________________________________________________________
// DESCRIPTION
// Contains code to generate two half sheets printed on one 8.5 x 11
// letter size sheet of paper. Accounts for a 1/2 left margin for
// binding
//______________________________________________________________________

//______________________________________________________________________
// TODO
//______________________________________________________________________
// half-letter-portrait and half-letter-landscape have a lot of
// duplicate code - these should be refactored to eliminate
// duplication.
//______________________________________________________________________

//______________________________________________________________________
// CONSTANTS
//______________________________________________________________________
// Note: This file uses constants from an external file. The html that
// calls this script should first list the constants file before
// listing this file.
//______________________________________________________________________
const letter_wdth_portrait_in  = 8.5;
const letter_hght_portrait_in  = 11;

const letter_wdth_portrait_px  = DPI * letter_wdth_portrait_in;
const letter_hght_portrait_px  = DPI * letter_hght_portrait_in;

//______________________________________________________________________
// Margins
//______________________________________________________________________

// To account for left binding
const std_margin_in     = 0.25;
const binder_margin_in  = 0.5;

const l_margin_in       = std_margin_in;
const r_margin_in       = std_margin_in;
const b_margin_in       = std_margin_in;

let t_margin_in       = 0;

// Change margin sides depending on double-sided print
if (DOUBLE_SIDED)
{
  t_margin_in       = std_margin_in;
}
else
{
  t_margin_in       = binder_margin_in;
}

// Convert in to px
const std_margin_px     = std_margin_in     * DPI;
const binder_margin_px  = binder_margin_in  * DPI;

const l_margin_px = l_margin_in * DPI;
const r_margin_px = r_margin_in * DPI;
const t_margin_px = t_margin_in * DPI;
const b_margin_px = b_margin_in * DPI;


//______________________________________________________________________
// Content Dimensions
//______________________________________________________________________

// Width of middle column that serves as margin
// Will account for two binder margins if printing double sided
let mid_margin_hght = 0;

if (DOUBLE_SIDED)
{
  mid_margin_hght = 2 * binder_margin_px;
}
else
{
  mid_margin_hght = t_margin_px + b_margin_px;
}

// Create whole letter
let letter_size_div = document.createElement("div");
letter_size_div.style.width   = letter_wdth_portrait_px + "px";
letter_size_div.style.height  = letter_hght_portrait_px + "px";
//letter_size_div.style.border  = DEBUG0_BORDER_STYLE;

let letter_content_div = document.createElement("div");
letter_content_div.style.width  = "100%";
letter_content_div.style.height = "100%";
//letter_content_div.style.border = DEBUG0_BORDER_STYLE;

// Set content margins through padding
letter_size_div.style.margin        = "0px";
letter_size_div.style.paddingTop    = t_margin_px + "px";
letter_size_div.style.paddingBottom = b_margin_px + "px";
letter_size_div.style.paddingLeft   = l_margin_px + "px";
letter_size_div.style.paddingRight  = r_margin_px + "px";

document.getElementById("content-container")
  .appendChild(letter_size_div);

letter_size_div.appendChild(letter_content_div);

let content_table   = document.createElement("table");

let top_content_row = document.createElement("tr");
let mddl_margin_row = document.createElement("tr");
let bot_content_row = document.createElement("tr");

let top_content_box = document.createElement("td");
let mddl_margin_box = document.createElement("td");
let bot_content_box = document.createElement("td");

letter_content_div.appendChild(content_table);

content_table.appendChild(top_content_row);
content_table.appendChild(mddl_margin_row);
content_table.appendChild(bot_content_row);

top_content_row.appendChild(top_content_box);
mddl_margin_row.appendChild(mddl_margin_box);
bot_content_row.appendChild(bot_content_box);

content_table.style.width   = "100%";
top_content_row.style.width = "100%";
mddl_margin_row.style.width = "100%";
bot_content_row.style.width = "100%";

content_table.style.height   = "100%";
top_content_row.style.height = "auto";
mddl_margin_row.style.height = mid_margin_hght + "px";
bot_content_row.style.height = "auto";

//content_table.style.border   = DEBUG1_BORDER_STYLE;
top_content_box.style.border = CONTENT_BORDER_STYLE;
//mddl_margin_box.style.border = DEBUG1_BORDER_STYLE;
bot_content_box.style.border = CONTENT_BORDER_STYLE;

top_content_box.style.padding = "0px";
mddl_margin_box.style.padding = "0px";
bot_content_box.style.padding = "0px";
