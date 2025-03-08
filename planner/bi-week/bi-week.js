//______________________________________________________________________
//______________________________________________________________________
//      _   __   _   _ _   _   _   _         _
// |   |_| | _  | | | V | | | | / |_/ |_| | /
// |__ | | |__| |_| |   | |_| | \ |   | | | \_
//  _  _         _ ___  _       _ ___   _                    / /
// /  | | |\ |  \   |  | / | | /   |   \                    (^^)
// \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
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
// Bi weekly calendar with goals.
//
// NOTE
// Intended to be used with constants.js and half-letter-landscape.js
//______________________________________________________________________

//______________________________________________________________________
// Style Constants
//______________________________________________________________________
const calendar_border_color = CONTENT_BORDER_COLOR;
const date_box_width        = `25px`;
const date_box_height       = `25px`;
const date_box_border_style = `1px solid ${calendar_border_color}`;

//______________________________________________________________________
function init_styles ()
{
  const day_border_style = `1px solid ${CONTENT_BORDER_COLOR}`;
  const style = document.createElement('style');

  style.innerHTML =
  `
    .week-table
    {
      width : 100%;
      border  : ${day_border_style};
    }

    .week-table td
    {
      border  : ${day_border_style};
      padding : 0px;
      width   : auto;
      height  : 120px;
      vertical-align : top;
    }
  `;

  document.head.appendChild(style);
}


//______________________________________________________________________
// Create date box
//______________________________________________________________________
function create_date_box()
{
  let date_box    = document.createElement('div');

  date_box.style.border = date_box_border_style;
  date_box.style.width  = date_box_width;
  date_box.style.height = date_box_height;

  return date_box;
}


//______________________________________________________________________
function create_week_calendar(days)
{
  init_styles();

  let week_table = document.createElement('table');
  week_table.classList.add('week-table');

  let week_row   = document.createElement('tr');

  for (let i = 0; i < days; i++)
  {
    let cell = document.createElement('td');
    cell.appendChild(create_date_box());
    week_row.appendChild(cell);
  }

  week_table.appendChild(week_row);

  return week_table;
}

//______________________________________________________________________
function create_goal_table(parent)
{
  let goal_table = document.createElement('table');
  parent.appendChild(goal_table);

  goal_table.style.border = DEBUG0_BORDER_STYLE;
  goal_table.style.width = '100%';

  let row0 = document.createElement('tr');
  let row1 = document.createElement('tr');
  let row2 = document.createElement('tr');
  let row3 = document.createElement('tr');

  row0.style.height = 'auto';
  row1.style.height = 'auto';
  row2.style.height = 'auto';
  row3.style.height = 'auto';

  let cll0 = document.createElement('td');
  let cll1 = document.createElement('td');
  let cll2 = document.createElement('td');
  let cll3 = document.createElement('td');

  cll0.style.border = DEBUG1_BORDER_STYLE;
  cll1.style.border = DEBUG1_BORDER_STYLE;
  cll2.style.border = DEBUG1_BORDER_STYLE;
  cll3.style.border = DEBUG1_BORDER_STYLE;

  goal_table.appendChild(row0);
  goal_table.appendChild(row1);
  goal_table.appendChild(row2);
  goal_table.appendChild(row3);

  row0.appendChild(cll0);
  row1.appendChild(cll1);
  row2.appendChild(cll2);
  row3.appendChild(cll3);
}

//______________________________________________________________________
function create_bi_week_page()
{
  let bi_week_page = document.createElement('table');
  bi_week_page.style.width  = '100%';
  bi_week_page.style.height = '100%';

  let row0 = document.createElement('tr');
  let row1 = document.createElement('tr');
  let row2 = document.createElement('tr');
  let row3 = document.createElement('tr');

  let cll0 = document.createElement('td');
  let cll1 = document.createElement('td');
  let cll2 = document.createElement('td');
  let cll3 = document.createElement('td');

  row0.style.height = 'auto';
  row1.style.height = 'auto';
  row2.style.height = 'auto';
  row3.style.height = 'auto';

  row0.appendChild(cll0);
  row1.appendChild(cll1);
  row2.appendChild(cll2);
  row3.appendChild(cll3);

  bi_week_page.appendChild(row0);
  bi_week_page.appendChild(row1);
  bi_week_page.appendChild(row2);
  bi_week_page.appendChild(row3);

  cll0.appendChild(create_week_calendar(7));
  cll2.appendChild(create_week_calendar(7));

  return bi_week_page;
}

//______________________________________________________________________
top_content_box_box.appendChild(create_bi_week_page());
bot_content_box_box.appendChild(create_bi_week_page());
